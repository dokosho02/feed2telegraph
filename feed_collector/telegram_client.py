from telegram import Bot
from telegram.constants import ParseMode
from typing import Optional

class TelegramClient:
    def __init__(self, bot_token: str):
        self.bot = Bot(token=bot_token)

    async def send_message(
        self,
        chat_id: str,
        title: str,
        link: str,
        telegraph_url: str
    ) -> Optional[bool]:
        try:
            message = (
                f"<b>{title}</b>\n"
                f"🔗 <a href='{link}'>Link</a>\t\t📖 <a href='{telegraph_url}'>Instant View</a>"
            )

            return await self.bot.send_message(
                chat_id=chat_id,
                text=message,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except Exception as e:
            print(f"⚠️ Failed to send Telegram message: {e}")
            return None
