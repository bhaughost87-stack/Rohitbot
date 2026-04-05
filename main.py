import os
import threading
from flask import Flask
from pyrogram import Client
from pyrogram.types import ChatJoinRequest

# --- RENDER PORT BINDING (Fixes Deploy Fail) ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health_check():
    return "Bot is active!"

def run_flask():
    # Render ko 10000 port chahiye hota hai deploy success karne ke liye
    flask_app.run(host='0.0.0.0', port=10000)

# --- TERA DATA ---
API_ID = 30141094
API_HASH = "edb173924ee7640a463f2484332041d7"
BOT_TOKEN = "7732935571:AAEpo4NO_EaRh17tvq5UMQ0LoT20xWZYnrk"
# Teri updated APK ID
APK_ID = "BQACAgUAAxkDAAMXadlkXxrwjBfVTOk3G-NRrtKt9YoAAq0aAALjflFWa0EWTZiLPYgeBA"

# TERA NAYA CAPTION
NEW_CAPTION = (
    "🎉 ( ONLY FOR PREMIUM USERS  ) 💥( 100% LOSS RECOVER GUARANTEE ) 😵\n"
    "Hack future add ☠️\n"
    "Wingo-Number Hack\n"
    "Trx1Min-Number Hack\n\n"
    "     💸Click and install💸"
)

app = Client("rohit_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- ONLY SEND APK (NO AUTO-APPROVE) ---
@app.on_chat_join_request()
async def send_apk(client, request: ChatJoinRequest):
    try:
        # Note: Yahan koi approve wali line nahi hai
        await client.send_document(
            chat_id=request.from_user.id, 
            document=APK_ID, 
            caption=NEW_CAPTION
        )
        print(f"✅ APK Sent to: {request.from_user.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

# NOTE: Is code mein 'on_message' handler nahi hai, isliye ID messages nahi aayenge.

if __name__ == "__main__":
    # Flask start port fix ke liye
    threading.Thread(target=run_flask).start()
    app.run()
