#!/usr/bin/env python3
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import aiohttp
import feedparser
from html_telegraph_poster import TelegraphPoster
from telegram import Bot
from telegram.constants import ParseMode
from tqdm import tqdm

# --- 智能路径探测 ---
def find_project_root(marker: str = ".env") -> Path:
    """自动定位项目根目录（根据.env文件）"""
    current = Path(__file__).absolute().parent  # 从当前文件位置开始
    max_depth = 10  # 防止无限循环
    while max_depth > 0:
        if (current / marker).exists():
            return current
        if current.parent == current:  # 到达文件系统根目录
            break
        current = current.parent
        max_depth -= 1
    raise FileNotFoundError(
        f"无法定位项目根目录（找不到 {marker} 文件）\n"
        "请确保：\n"
        "1. 项目根目录包含 .env 文件\n"
        "2. 从项目目录或其子目录运行"
    )

# --- 初始化全局路径 ---
try:
    PROJECT_ROOT = find_project_root()
    DATA_DIR = PROJECT_ROOT / "data"
    DATA_DIR.mkdir(exist_ok=True)  # 确保数据目录存在
    HISTORY_FILE = DATA_DIR / "rss_updates.json"
except Exception as e:
    print(f"❌ 初始化失败: {e}", file=sys.stderr)
    sys.exit(1)

# --- 主逻辑类 ---
class RSS2Telegram:
    def __init__(self):
        # 加载环境变量
        from dotenv import load_dotenv
        load_dotenv(PROJECT_ROOT / ".env")  # 从根目录加载

        # 验证必要配置
        self.rss_url = os.getenv("RSS_URL")
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.channel_id = os.getenv("TELEGRAM_CHANNEL")
        if not all([self.rss_url, self.bot_token, self.channel_id]):
            raise ValueError(
                "缺少必要的环境变量！请检查：\n"
                "RSS_URL, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL"
            )

        # 初始化组件
        self.telegraph = TelegraphPoster(use_api=True)
        self.telegraph.create_api_token("RSSBot")
        self.bot = Bot(token=self.bot_token)
        self.session = aiohttp.ClientSession()
        self.history = self._load_history()

    def _load_history(self) -> Dict[str, dict]:
        """加载处理历史记录"""
        try:
            if HISTORY_FILE.exists():
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"⚠️ 加载历史记录失败: {e}", file=sys.stderr)
            return {}

    def _save_history(self):
        """保存处理记录"""
        try:
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ 保存历史记录失败: {e}", file=sys.stderr)

    async def _create_telegraph_page(self, entry: dict) -> Optional[str]:
        """生成Telegraph页面"""
        try:
            content = f"<h1>{entry.get('title', 'Untitled')}</h1>"

            # 兼容不同RSS格式
            if entry.get("content"):
                content += entry["content"][0]["value"]
            elif entry.get("description"):
                content += entry["description"]

            # 添加原文链接
            content += f'<p><a href="{entry.get("link", "")}">🔗 Link</a></p>'

            response = self.telegraph.post(
                title=entry.get("title", "RSS内容")[:128],  # 标题长度限制
                author="Feed Bot",
                text=content,
            )
            return f"https://telegra.ph/{response['path']}"
        except Exception as e:
            print(f"⚠️ 创建Telegraph页面失败: {e}", file=sys.stderr)
            return None

    async def _send_to_telegram(self, title: str, link: str, telegraph_url: str):
        """发送消息到Telegram频道"""
        try:
            message = (
                f"<b>{title}</b>\n\n"
                f"📖 <a href='{telegraph_url}'>Instant View</a>\n"
                f"🔗 <a href='{link}'>Link</a>"
            )

            await self.bot.send_message(
                chat_id=self.channel_id,
                text=message,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except Exception as e:
            print(f"⚠️ 发送Telegram消息失败: {e}", file=sys.stderr)

    async def fetch_rss(self) -> List[dict]:
        """获取并解析RSS内容"""
        try:
            async with self.session.get(self.rss_url) as response:
                if response.status != 200:
                    raise ValueError(f"RSS请求失败: HTTP {response.status}")

                content = await response.text()
                feed = feedparser.parse(content)

                if feed.get("bozo_exception"):
                    raise ValueError(f"RSS解析错误: {feed.bozo_exception}")

                return [
                    {
                        "id": entry.get("id", entry.get("link", "")),
                        "title": entry.get("title", "无标题"),
                        "link": entry.get("link", ""),
                        "published": entry.get("published", ""),
                        "content": entry.get("content", []),
                        "description": entry.get("description", ""),
                    }
                    for entry in feed.entries
                ]
        except Exception as e:
            print(f"⚠️ 获取RSS内容失败: {e}", file=sys.stderr)
            return []

    async def process(self):
        """主处理流程"""
        print(f"🔍 开始处理 RSS: {self.rss_url}")
        entries = await self.fetch_rss()
        if not entries:
            print("ℹ️ 未获取到有效内容", file=sys.stderr)
            return

        # 过滤新条目
        new_entries = [e for e in entries if e["id"] not in self.history]
        if not new_entries:
            print("✅ 没有新内容需要处理")
            return

        print(f"📥 发现 {len(new_entries)} 条新内容")

        # 处理进度条
        progress = tqdm(new_entries, desc="处理进度", unit="条")
        success_count = 0

        for entry in progress:
            try:
                telegraph_url = await self._create_telegraph_page(entry)
                if not telegraph_url:
                    continue

                await self._send_to_telegram(
                    title=entry["title"],
                    link=entry["link"],
                    telegraph_url=telegraph_url
                )

                # 记录处理状态
                self.history[entry["id"]] = {
                    "title": entry["title"],
                    "link": entry["link"],
                    "telegraph": telegraph_url,
                    "processed_at": datetime.now().isoformat()
                }
                success_count += 1
            except Exception as e:
                progress.write(f"⚠️ 处理失败 [{entry['title']}]: {e}")

        # 保存记录
        if success_count > 0:
            self._save_history()
            print(f"🎉 成功处理 {success_count}/{len(new_entries)} 条内容")
        else:
            print("❌ 所有条目处理失败", file=sys.stderr)

    async def close(self):
        """资源清理"""
        await self.session.close()

# --- 主入口 ---
async def main():
    bot = None
    try:
        bot = RSS2Telegram()
        await bot.process()
    except Exception as e:
        print(f"❌ 程序崩溃: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if bot:
            await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
