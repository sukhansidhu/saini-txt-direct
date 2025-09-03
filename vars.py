# 🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button

import os
from os import environ

# Telegram API details
API_ID = int(environ.get("API_ID", "25331263"))
API_HASH = environ.get("API_HASH", "cab85305bf85125a2ac053210bcd1030"))
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner / Admin details
OWNER = int(environ.get("OWNER", "1955406483"))
CREDIT = environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")

# Users setup
TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1955406483').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]

# Ensure OWNER is always authorized
if OWNER not in AUTH_USERS:
    AUTH_USERS.append(OWNER)

# Webhook config (optional)
# WEBHOOK = True  # Don't change this
# PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

