import os
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

# --- CONFIGURATION ---
API_ID = int(os.environ.get("API_ID", "30141094"))
API_HASH = os.environ.get("API_HASH", "edb173924ee7640a463f2484332041d7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7732935571:AAEpo4NO_EaRh17tvq5UMQ0LoT20xWZYnrk")

# Teri APK File ID jo tune Termux se nikali hai
APK_FILE_ID = "BQACAgUAAxkBAAMHadEVOlUCXj8zQCOcgsaJDyX52b0AAq0aAALjflFWa0EWTZiLPYgeBA"

CAPTION_MSG = (
    "🔴 **LIVE ( 1/1 ) SESSION📈**\n"
    "       ( Personal Session )\n\n"
    "✅ **Real Loss Recovery**\n"
    "✅ **Non Mtg Signals**\n"
    "✅ **100% Refund (if loss)**\n"
    "✅ **Free Session**\n\n"
    "**Message for Your Loss recovery 📈**\n"
    "👉 https://t.me/Rd_2019_01 📩"
)

app = Client("dost_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Auto Approve Function
@app.on_chat_join_request()
async def auto_approve(client, message: ChatJoinRequest):
    try:
        # Request accept karna
        await client.approve_chat_join_request(chat_id=message.chat.id, user_id=message.from_user.id)
        
        # User ko APK aur Message bhejna
        await client.send_document(
            chat_id=message.from_user.id, 
            document=APK_FILE_ID, 
            caption=CAPTION_MSG
        )
        print(f"✅ Approved & Sent: {message.from_user.first_name}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Bot ko start karne ka seedha tarika
if __name__ == "__main__":
    app.run()

