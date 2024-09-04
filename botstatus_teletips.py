from pyrogram import Client, filters, idle
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os, uvloop

uvloop.install()
loop = asyncio.get_event_loop()

app = Client(
    name = "cheems",
    api_id = int(os.environ.get("API_ID", "6")),
    api_hash = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e"),
    session_string = os.environ.get("SESSION_NAME", "BQAS828AaYPna-g2hqevY61V8x4kcNt4hHY4Ixqs8FncZBWbGGiDIX92qMMsbB3pg755XzuPd7hbVCK8f_FYZ2KTyunWBXH1WUKDArbczxadyYQ-WS2x6a6N-SydydAkR-W0j3oymhPsXT8kBgrkHodetpm5t0pyPqWHZchj0p9QWBlAX-QiGpEy4Ukf-cC_GNnX5kFvPGbUpyMv_mHI6925qDScfQPRwMHe0vC2C0EQjf9ZmeQAk5kUvxdj1HZDQjP4k_R15besxpIdOKdRI7AoPHI_xja0zntNfFQjujL2tC1ak8GI69-8U11AgZAIRMCMykKepdL0gZgcZ6SejJWaz5tS7wAAAAEu5gwJAA")
)

TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST", "cheemsvcbot CheemsChatBot CheemsMovieRobot LinkFilesBot TeraDLRobot TeraBoxLeechRoBot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ.get("CHANNEL_OR_GROUP_ID", "-1001863324887"))
MESSAGE_ID = int(os.environ.get("MESSAGE_ID", "2"))
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS", "5545068262").split(' ')]

async def main_teletips():
            while True:
                await asyncio.sleep(2)
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_teletips = f"📊 **<u>CHEEMS STATUS</u>**"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(20)
                        async for zzz_teletips in app.get_chat_history(bot, limit = 1):                        
                         bbb = zzz_teletips.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n\n🔴 **STATUS**: down ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                        else:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n\n🟢 **STATUS**: alive ✅"                     
                    except FloodWait as e:
                        await asyncio.sleep(e.v)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y")
                last_upstat = time.strftime(f"%I:%M %p")
                xxx_teletips += f"\n\n**--Last checked on:--**\nDate: {last_update}\nTime: {last_upstat} IST</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(600)


async def init():
  await app.start()
  asyncio.create_task(main_teletips())
  await idle()
  
if __name__ == "__main__":
    loop.run_until_complete(init())
