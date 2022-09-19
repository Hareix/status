#pylint:disable=C0301
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    api_id = int(os.environ.get("API_ID", "6")),
    api_hash = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e"),
    session_name = os.environ.get("SESSION_NAME", "AQC43rnvWI4C_XGuL_CO2ZUJmhIjKKygNKVBEeljSVNXlUeonwIPoPqz-vg4NrFTFXEoOTUEBz5aLhk7AqF36kNt0CO6ZCDXbzCP4bXJKFTpFYKEzNCr-NAHLlL5dXaGGaSCcQGwJ8niI4kAMZaPWj49Ezy0j66YH5brlBlILOclYYI3jrgNVvkQi-dl-N21K9N-0gQHrb-h4i73BTKDh47b9KCjis6Tg5dE0x7HioY8r1QisMzSAJfpbk9DzvEwIwRM9qLjBYPM2Dn-4fdZpXDVzKe0ytn3sLk-yN9AB3bqmvITg2z-ThW63QH0MBPymtWanW1gnrAGpZx2U0VDPqRsAAAAAVHU63sA")
)
TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST", "cheemsvideorobot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ.get("CHANNEL_OR_GROUP_ID", "-1001593056689"))
MESSAGE_ID = int(os.environ.get("MESSAGE_ID", "17680"))
BOT_ADMIN_ID = 5545068262

async def main_teletips():
    async with app:
            while True:
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_teletips = f"📊 **<u>CHEEMS STATUS</u>**"
                for bot in BOT_LIST:
                    try:
                        await app.send_message(bot, "/respondtocheemschecker")
                        print("Checking")
                        await asyncio.sleep(20)
                for bot in BOT_LIST:
                          print(bot)
                          async for mssg in app.search_messages(bot, "", limit=1):
                            if str(mssg.text) == str("/respondtocheemschecker"):
                                xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n\n🔴 **STATUS**: down ❌"
                                try:
                                    await app.send_message(int(BOT_ADMIN_ID), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            else:
                              text = mssg.text
                              cpu = text.split("_+_")[0]
                              chats = text.split("_+_")[1]
                              users = text.split("_+_")[2]
                              playlist = text.split("_+_")[3]
                              active = text.split("_+_")[4]
                              xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n\n🟢 **STATUS**: online ✅\n\n**🎛️ Server Load**: {cpu}\n\n**🎵 Active Voice Calls**: {active}\n\n**📈 Served Chats**: {chats}\n\n**👤 Served Users**: {users}\n\n**🎶 Total Playlists** {playlist}"
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y")
                last_upstat = time.strftime(f"%I:%M %p")
                xxx_teletips += f"\n\nLast checked on:\nDate: {last_update}\nTime: {last_upstat} IST</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(600)
                        
app.run(main_teletips())
