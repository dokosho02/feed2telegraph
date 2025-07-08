from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class RSSEntry:
    id: str
    title: str
    link: str
    published: str
    content: List[Dict]
    description: str

@dataclass
class ProcessedEntry:
    title: str
    link: str
    telegraph_url: str
    processed_at: str
