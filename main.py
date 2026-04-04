import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

# --- RENDER FREE TIER FIX (DHOKA SERVER) ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health_check():
    return "Bot is active and running!"

def run_flask():
    # Render port 10000 mangta hai free tier ke liye
    flask_app.run(host='0.0.0.0', port=10000)

# --- BOT CONFIGURATION ---
API_ID = int(os.environ.get("API_ID", "30141094"))
API_HASH = os.environ.get("API_HASH", "edb173924ee7640a463f2484332041d7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7732935571:AAEpo4NO_EaRh17tvq5UMQ0LoT20xWZYnrk")

# Nayi APK ID jo tune abhi bheji
APK_FILE_ID = "BQACAgUAAxkBAAMFadENsc3tF6KtrPwTlhOte_gY5HkAAq0aAALjflFWa0EWTZiLPYgeBA"

# Naya Caption aur Naya DM Link
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

# --- AUTO APPROVE LOGIC ---
@app.on_chat_join_request()
async def auto_approve(client, message: ChatJoinRequest):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    try:
        # 1. Request Approve karo
        await client.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
        
        # 2. User ko APK aur Naya Message bhejo
        await client.send_document(
            chat_id=user_id,
            document=APK_FILE_ID,
            caption=CAPTION_MSG
        )
        print(f"✅ Approved & APK Sent to: {message.from_user.first_name}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# ID nikalne ke liye (Tujhe DM mein reply dega agar kuch bhejoge)
@app.on_message(filters.document | filters.video)
async def get_ids(client, message):
    file_id = message.document.file_id if message.document else message.video.file_id
    await message.reply_text(f"Bhai ID mil gayi, isse code mein dalo:\n\n`{file_id}`")

if __name__ == "__main__":
    # Flask ko background mein chalao taaki Render "Timeout" na kare
    threading.Thread(target=run_flask).start()
    # Bot start karo
    print("🚀 Bot starting on Render...")
    app.run()

