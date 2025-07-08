import os
from pathlib import Path
from typing import Dict

def find_project_root() -> Path:
    current = Path(__file__).absolute().parent
    max_depth = 10
    while max_depth > 0:
        if (current / ".env").exists() or (current / "pyproject.toml").exists():
            return current
        if current.parent == current:
            break
        current = current.parent
        max_depth -= 1

    if 'GITHUB_WORKSPACE' in os.environ:
        return Path(os.environ['GITHUB_WORKSPACE'])
    raise FileNotFoundError("Cannot locate project root")

def load_config() -> Dict[str, str]:
    is_ci = os.getenv('GITHUB_ACTIONS') == 'true'
    config = {}

    if not is_ci:
        from dotenv import load_dotenv
        env_path = find_project_root() / ".env"
        if env_path.exists():
            load_dotenv(env_path)

    required_keys = {
        'rss_url': os.getenv("RSS_URL"),
        'bot_token': os.getenv("TELEGRAM_BOT_TOKEN"),
        'channel_id': os.getenv("TELEGRAM_CHANNEL"),
    }

    if not all(required_keys.values()):
        missing = [k for k, v in required_keys.items() if not v]
        raise ValueError(f"Missing config: {missing}")

    return required_keys
