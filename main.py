import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

# --- DUMMY SERVER FOR RENDER FREE TIER ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health_check():
    return "Bot is running!"

def run_flask():
    # Render port 10000 mangta hai
    flask_app.run(host='0.0.0.0', port=10000)

# --- BOT CONFIG ---
API_ID = int(os.environ.get("API_ID", "30141094"))
API_HASH = os.environ.get("API_HASH", "edb173924ee7640a463f2484332041d7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7732935571:AAEpo4NO_EaRh17tvq5UMQ0LoT20xWZYnrk")
APK_FILE_ID = "BQACAgUAAxkBAAMHadEVOlUCXj8zQCOcgsaJDyX52b0AAq0aAALjflFWa0EWTZiLPYgeBA"

app = Client("dost_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def auto_approve(client, message: ChatJoinRequest):
    try:
        await client.approve_chat_join_request(chat_id=message.chat.id, user_id=message.from_user.id)
        await client.send_document(chat_id=message.from_user.id, document=APK_FILE_ID, caption="Apka APK ye raha!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Flask ko background mein chalao taaki Render khush rahe
    threading.Thread(target=run_flask).start()
    # Bot start karo
    app.run()
