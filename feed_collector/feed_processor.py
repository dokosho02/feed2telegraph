import feedparser
from html_telegraph_poster import TelegraphPoster
from typing import List, Optional
from .models import RSSEntry

class FeedProcessor:
    def __init__(self):
        self.telegraph = TelegraphPoster(use_api=True)
        self.telegraph.create_api_token("FeedBot")

    async def parse_feed(self, rss_url: str) -> List[RSSEntry]:
        try:
            feed = feedparser.parse(rss_url)
            if feed.get("bozo_exception"):
                raise ValueError(f"RSS parse error: {feed.bozo_exception}")

            return [
                RSSEntry(
                    id=entry.get("id", entry.get("link", "")),
                    title=entry.get("title", "Untitled"),
                    link=entry.get("link", ""),
                    published=entry.get("published", ""),
                    content=entry.get("content", []),
                    description=entry.get("description", ""),
                )
                for entry in feed.entries
            ]
        except Exception as e:
            print(f"⚠️ Failed to parse feed: {e}")
            return []

    def create_telegraph_page(self, entry: RSSEntry) -> Optional[str]:
        try:
            content = f"<h1>{entry.title}</h1>"
            content += f'<p><a href="{entry.link}">🔗 Link</a></p>'

            if entry.content:
                content += entry.content[0]["value"]
            elif entry.description:
                content += entry.description

            response = self.telegraph.post(
                title=entry.title[:128],
                author="Feed Bot",
                text=content,
            )
            return f"https://telegra.ph/{response['path']}"
        except Exception as e:
            print(f"⚠️ Failed to create Telegraph page: {e}")
            return None
