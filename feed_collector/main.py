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


# --- 智能路径探测（兼容本地和CI）---
def find_project_root() -> Path:
    # 自动定位项目根目录
    current = Path(__file__).absolute().parent
    max_depth = 10
    while max_depth > 0:
        # 检查常见项目标记文件
        if (current / ".env").exists() or (current / "pyproject.toml").exists():
            return current
        if current.parent == current:
            break
        current = current.parent
        max_depth -= 1

    # GitHub Actions 环境回退
    if 'GITHUB_WORKSPACE' in os.environ:
        return Path(os.environ['GITHUB_WORKSPACE'])

    raise FileNotFoundError("无法定位项目根目录")

# --- 配置加载器 ---
def load_config():
    # 智能加载配置（本地用.env，CI用secrets）
    is_ci = False
    is_ci = os.getenv('GITHUB_ACTIONS') == 'true'
    config = {}

    if not is_ci:
        # 本地开发：从.env加载
        from dotenv import load_dotenv
        env_path = find_project_root() / ".env"
        if env_path.exists():
            load_dotenv(env_path)
        else:
            print("⚠️ 本地提示：未找到.env文件，将尝试从环境变量读取")

    # 通用加载逻辑
    config.update({
        'rss_url': os.getenv("RSS_URL"),
        'bot_token': os.getenv("TELEGRAM_BOT_TOKEN"),
        'channel_id': os.getenv("TELEGRAM_CHANNEL"),
        # 'is_ci': is_ci
    })

    # print(config)

    # 验证必要配置
    if not all(config.values()):
        missing = [k for k, v in config.items() if not v]
        raise ValueError(f"缺少配置: {missing}\n"
                       "GitHub Actions 请检查 secrets，本地开发请检查 .env 文件")

    return config

# --- 初始化 ---
try:
    PROJECT_ROOT = find_project_root()
    # DATA_DIR = PROJECT_ROOT / "data"
    DATA_DIR = Path("data")
    DATA_DIR.mkdir(exist_ok=True)
    HISTORY_FILE = DATA_DIR / "rss_updates.json"

    print(f"history file in python file - {HISTORY_FILE}")
    CONFIG = load_config()  # 加载配置
except Exception as e:
    print(f"❌ 初始化失败: {e}", file=sys.stderr)
    sys.exit(1)


# --- 主逻辑类 ---
class RSS2Telegram:
    def __init__(self):
        # 直接使用已加载的配置
        self.rss_url    = CONFIG['rss_url']
        self.bot_token  = CONFIG['bot_token']
        self.channel_id = CONFIG['channel_id']

        # 初始化组件
        # telegraph
        self.telegraph = TelegraphPoster(use_api=True)
        self.telegraph.create_api_token("FeedBot")

        # telegram not
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
            # 添加原文链接
            content += f'<p><a href="{entry.get("link", "")}">🔗 Link</a></p>'

            # 兼容不同RSS格式
            if entry.get("content"):
                content += entry["content"][0]["value"]
            elif entry.get("description"):
                content += entry["description"]


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
                f"<b>{title}</b>\n"
                f"🔗 <a href='{link}'>Link</a>\t\t📖 <a href='{telegraph_url}'>Instant View</a>"
            )

            await self.bot.send_message(
                chat_id=self.channel_id,
                text=message,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except Exception as e:
            print(f"⚠️ 发送Telegram消息失败: {e}", file=sys.stderr)

    async def fetch_feed(self) -> List[dict]:
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
        entries = await self.fetch_feed()
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
