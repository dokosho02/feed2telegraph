import asyncio
import sys
from tqdm import tqdm
from .config import load_config, find_project_root
from .storage import HistoryStorage
from .feed_processor import FeedProcessor
from .telegram_client import TelegramClient
from .models import RSSEntry

class RSS2Telegram:
    def __init__(self):
        self.config = load_config()
        self.storage = HistoryStorage(
            find_project_root() / "data" / "rss_updates.json"
        )
        self.feed_processor = FeedProcessor()
        self.telegram_client = TelegramClient(self.config['bot_token'])
        self.history = self.storage.load()

    async def process(self):
        print(f"🔍 Processing RSS: {self.config['rss_url']}")
        entries = await self.feed_processor.parse_feed(self.config['rss_url'])
        if not entries:
            print("ℹ️ No valid content found")
            return

        new_entries = [e for e in entries if e.id not in self.history]
        if not new_entries:
            print("✅ No new content to process")
            return

        print(f"📥 Found {len(new_entries)} new entries")
        progress = tqdm(new_entries, desc="Processing", unit="entry")
        success_count = 0

        for entry in progress:
            try:
                telegraph_url = self.feed_processor.create_telegraph_page(entry)
                if not telegraph_url:
                    continue

                await self.telegram_client.send_message(
                    chat_id=self.config['channel_id'],
                    title=entry.title,
                    link=entry.link,
                    telegraph_url=telegraph_url
                )

                self.history[entry.id] = {
                    "title": entry.title,
                    "link": entry.link,
                    "telegraph": telegraph_url,
                    "processed_at": datetime.now().isoformat()
                }
                success_count += 1
            except Exception as e:
                progress.write(f"⚠️ Processing failed [{entry.title}]: {e}")

        if success_count > 0:
            self.storage.save(self.history)
            print(f"🎉 Successfully processed {success_count}/{len(new_entries)} entries")
        else:
            print("❌ All entries failed to process")

async def main():
    processor = RSS2Telegram()
    try:
        await processor.process()
    except Exception as e:
        print(f"❌ Fatal error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
