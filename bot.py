import telebot
import time
from config import BOT_TOKEN, OWNER_ID, FORCE_CHANNEL, FORCE_GROUP, BOT_VERSION
from model import FridayAI
from utils import check_force_join, log_update

# 🔹 Bot initialize
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
friday = FridayAI()

# 🔹 /start command
@bot.message_handler(commands=["start"])
def start_handler(message):
    user_id = message.from_user.id

    # Force Join Check
    if not check_force_join(user_id, FORCE_CHANNEL, FORCE_GROUP, bot):
        bot.send_message(user_id, "⚠️ Please join required channel & group first!")
        return
    
    if user_id == OWNER_ID:
        welcome = f"👑 Welcome Master!\n🤖 Friday v{BOT_VERSION} is online!"
    else:
        welcome = f"✨ Welcome {message.from_user.first_name}!\n🤖 Friday v{BOT_VERSION} is online!"

    bot.send_message(user_id, welcome)

# 🔹 Auto Reply System
@bot.message_handler(func=lambda msg: True)
def auto_reply(message):
    user_id = message.from_user.id

    # Owner special handling
    if user_id == OWNER_ID:
        prefix = "👑 Master,"
    else:
        prefix = f"🙋 {message.from_user.first_name},"

    # AI response
    response = friday.respond(message.text)
    bot.send_chat_action(user_id, "typing")
    time.sleep(1)  # typing effect
    bot.send_message(user_id, f"{prefix}\n\n{response}")

# 🔹 Start Bot
print(f"Friday v{BOT_VERSION} is running...")
bot.infinity_polling()
