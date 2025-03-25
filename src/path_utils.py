from pathlib import Path
import os

def find_project_root(marker=".env"):
    try:
        current = Path(__file__).absolute()
        while True:
            if (current / marker).exists():
                return current
            if current.parent == current:
                break
            current = current.parent
        raise FileNotFoundError(
            f"未找到项目根目录（标记文件: {marker}）\n"
            "请确保：\n"
            "1. 项目包含 .env 文件\n"
            "2. 从项目目录或其子目录运行"
        )
    except Exception as e:
        print(f"❌ 路径解析失败: {e}")
        raise

def get_data_dir() -> Path:
    """获取跨环境兼容的数据目录"""
    root = find_project_root()
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir
