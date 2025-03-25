import os
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 基础路径配置
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# 确保数据目录存在
DATA_DIR.mkdir(exist_ok=True)

# 动态获取环境变量
def get_env(key, default=None):
    """安全获取环境变量"""
    value = os.getenv(key)
    if value is None and default is None:
        raise ValueError(f"Missing required environment variable: {key}")
    return value or default

# 核心配置
class Config:
    RSS_URL = get_env("RSS_URL")
    BOT_TOKEN = get_env("TELEGRAM_BOT_TOKEN")
    CHANNEL_ID = get_env("TELEGRAM_CHANNEL")
    HISTORY_FILE = DATA_DIR / "rss_updates.json"

# 环境检测
def is_github_actions():
    return os.getenv("GITHUB_ACTIONS") == "true"
