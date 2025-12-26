import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Telegram Bot Configuration
# Railway KATTA HARF ishlatadi, local kichik harf
BOT_TOKEN = os.getenv("BOT_TOKEN") or os.getenv("bot_token")

# Admin ID
admin_id_str = os.getenv("ADMIN_ID") or os.getenv("admin_id") or "0"
ADMINS = [int(admin_id_str)]

# Database fayl nomi
DATABASE_NAME = "kino_bot.db"

# Kanal (ixtiyoriy) - foydalanuvchilar a'zo bo'lishi kerak bo'lgan kanal
CHANNEL_USERNAME = None  # Masalan: "@your_channel"
CHANNEL_ID = None  # Masalan: -1001234567890
