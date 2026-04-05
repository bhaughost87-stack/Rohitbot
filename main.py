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
    # Ye Render ko signal deta hai ki bot zinda hai
    flask_app.run(host='0.0.0.0', port=10000)

# --- BOT CONFIG ---
API_ID = 30141094
API_HASH = "edb173924ee7640a463f2484332041d7"
BOT_TOKEN = "7732935571:AAEpo4NO_EaRh17tvq5UMQ0LoT20xWZYnrk"
# Teri updated APK ID
APK_ID = "BQACAgUAAxkBAAMHadEVOlUCXj8zQCOcgsaJDyX52b0AAq0aAALjflFWa0EWTZiLPYgeBA"

# TERA NAYA CAPTION
NEW_CAPTION = (
    "🎉 ( ONLY FOR PREMIUM USERS  ) 💥( 100% LOSS RECOVER GUARANTEE ) 😵\n"
    "Hack future add ☠️\n"
    "Wingo-Number Hack\n"
    "Trx1Min-Number Hack\n\n"
    "     💸Click and install💸"
)

app = Client("auto_sender", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def send_apk(client, request: ChatJoinRequest):
    try:
        # Note: Approve wali line yahan nahi hai, isliye request pending rahegi
        # Seedha User ko inbox mein APK aur Naya Caption bhejo
        await client.send_document(
            chat_id=request.from_user.id, 
            document=APK_ID, 
            caption=NEW_CAPTION
        )
        print(f"✅ APK Sent to: {request.from_user.id} (Request Pending)")
    except Exception as e:
        print(f"❌ Error: {e}")

# NOTE: Yahan 'on_message' wala koi function nahi hai, isliye "Bhai ID mil gayi" nahi aayega.

if __name__ == "__main__":
    # Flask ko background thread mein chalao
    threading.Thread(target=run_flask).start()
    print("🚀 Bot LIVE hai! Naya Caption set kar diya gaya hai.")
    app.run()
