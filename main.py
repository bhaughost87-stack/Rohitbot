import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

# --- RENDER PORT FIX ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health_check():
    return "Bot is active!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=10000)

# --- BOT CONFIG ---
API_ID = int(os.environ.get("API_ID", "30141094"))
API_HASH = os.environ.get("API_HASH", "edb173924ee7640a463f2484332041d7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7732935571:AAEpo4NO_EaRh17tvq5UMQ0LoT20xWZYnrk")

# Teri Nayi APK ID
APK_FILE_ID = "BQACAgUAAxkDAAMSadErzNbwNtV802jrAgfwu9YazmYAAq0aAALjflFWa0EWTZiLPYgeBA"

CAPTION_MSG = (
    "🔴 **LIVE ( 1/1 ) SESSION📈**\n"
    "       ( Personal Session )\n\n"
    "✅ **Real Loss Recovery**\n"
    "✅ **Non Mtg Signals**\n"
    "✅ **100% Refund (if loss)**\n"
    "✅ **Free Session**\n\n"
    "**Message for Your Loss recovery 📈**\n"
    "👉 https://t.me/Rd_hereee 📩"
)

app = Client("rohit_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- ONLY SEND APK (NO AUTO-APPROVE) ---
@app.on_chat_join_request()
async def send_only_apk(client, message: ChatJoinRequest):
    try:
        # Note: Approve wali line yahan se hatayi gayi hai
        await client.send_document(
            chat_id=message.from_user.id,
            document=APK_FILE_ID,
            caption=CAPTION_MSG
        )
        print(f"✅ APK Sent to: {message.from_user.first_name} (Request Pending)")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print("🚀 Starting Bot (Manual Request Mode)...")
    app.run()
