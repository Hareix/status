from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    api_id = int(os.environ["API_ID"], ["19335070"]),
    api_hash = os.environ["API_HASH", "36e8b8709cf6579f11559692b70f0c46"],
    session_name = os.environ["SESSION_NAME", "AQC0FAJf0W3QTtZL9gHLZfxmZRHQhpMBpdGgLclWepY0S-iIh7zFh1LIhkT4HRjNBfo8PJtc_Bk2PEMHb8bQX1AKxY3hyagDXd2k6LLE3aN077h-1tMcoPHAhY0PeejmVUfJUOzEjsZWrgUUpRf67JcLsvBfvB6o5FR9vdUubc9-Q5P5JZlWFLv2jPvXffLLFBTQpmXPWQ_O9-TPhH_n26ApOuEtyBhiRyrGJkj7g4WM2mh8W-Fwn43v99cyi3lYoZsb0U0uLjMy8ja2CWtUNm6wzldM8JlHDMchJnt5Gz6MdVla7VCZdGG3K7dyutP4cld7g_carPcFZ-o2ZVZjuPlZAAAAAVIiJMcA"]
)
TIME_ZONE = os.environ["TIME_ZONE", "Asia/Kolkata"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST", "@cheemsvcbot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID", "-1001361125382"])
MESSAGE_ID = int(os.environ["MESSAGE_ID", "216"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS", "5545068262").split(' ')]

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_teletips = f"📊 **<u>CHEEMS STATUS</u>**"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.message_id
                        await asyncio.sleep(10)
                        zzz_teletips = await app.get_history(bot, limit = 1)
                        for ccc in zzz_teletips:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n🔴 **STATUS**: down ❌"
                            await app.read_history(bot)
                        else:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n🟢 **STATUS**: alive ✅"
                            await app.read_history(bot)
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
