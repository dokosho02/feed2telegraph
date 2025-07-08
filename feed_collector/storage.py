import json
from pathlib import Path
from typing import Dict

class HistoryStorage:
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.storage_path.parent.mkdir(exist_ok=True)

    def load(self) -> Dict[str, dict]:
        try:
            if self.storage_path.exists():
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"⚠️ Failed to load history: {e}")
            return {}

    def save(self, data: Dict[str, dict]):
        try:
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Failed to save history: {e}")
