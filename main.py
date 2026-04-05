From pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

# TERA DATA
API_ID = 30141094
API_HASH = "edb173924ee7640a463f2484332041d7"
BOT_TOKEN = "7732935571:AAEpo4NO_EaRh17tvq5UMQ0LoT20xWZYnrk"

# TERA APK ID
APK_ID = "BQACAgUAAxkBAAMHadEVOlUCXj8zQCOcgsaJDyX52b0AAq0aAALjflFWa0EWTZiLPYgeBA"

app = Client("auto_sender", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def send_apk(client, request: ChatJoinRequest):
    try:
        # User ko inbox mein APK bhejo
        await client.send_document(
            chat_id=request.from_user.id, 
            document=APK_ID, 
            caption="🚀 **🎉 ( ONLY FOR PREMIUM USERS  ) 💥( 100% LOSS RECOVER GUARANTEE ) 😵
Hack future add ☠️
Wingo-Number Hack
Trx1Min-Number Hack

     💸Click and install💸

How To Use and download Hack 👇
https://t.me/JaiclubNumberHack/5
https://t.me/JaiclubNumberHack/5. 🔥"
        )
        print(f"✅ APK Sent to: {request.from_user.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 Bot LIVE hai! Jo bhi channel join request bhejega, use APK mil jayega.")
app.run()
 
