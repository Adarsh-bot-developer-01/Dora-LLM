import os

# 🔹 Bot Config
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
FORCE_CHANNEL = os.getenv("FORCE_CHANNEL")
FORCE_GROUP = os.getenv("FORCE_GROUP")

# 🔹 Bot Version
BOT_VERSION = "1.0.0"

# 🔹 Special Logging Group (future use)
DEV_LOG_GROUP = os.getenv("DEV_LOG_GROUP", OWNER_ID)
