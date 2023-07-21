from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os
from animdl.core.cli.commands.grab import animdl_grab
from aiohttp import web
import asyncio
import json
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

data_dict = {}
mongo = MongoClient("mongodb+srv://sneha:sneha@cluster0.zhphhyu.mongodb.net/?retryWrites=true&w=majority")
db = mongo.cheemsnsfk
streamdb = db.animestream

app = Client(
    api_id = int(os.environ.get("API_ID", "6")),
    api_hash = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e"),
    session_name = os.environ.get("SESSION_NAME", "BQBMvtKet134IGCmzPwuIcpIQ1W33Kr7tyUrspwnHjTWzwsG0mzxmsOlmQTobYsHAKDETHay069H0oCtyjv0DYve_naU945POe8qaR5s_uw2hYxYZWt9MYudraMp96xOMT98fOGqUSFI5SQgIL6N2mfH9dhsgTZOMhdRpO3amIn6fL3UtjfXN2EHFAJIoqx5qyZLcRogKmnnPZvUA-O2tapqXVfnIs4qxYObhJCpi3VAkQmYVcEH1dTsIX1GNysxK3M-0ZXEB23Rl6_rtNzpV0Z8CCvnZrocvbPmK2-H1AYCGmLQzER5GehrUCmVVsyv1BYII-NLDAXfsVbDYciZ0o6SAAAAAS7mDAkA")
)

TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST", "cheemsvcbot CheemsChatBot CheemsBobsBot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ.get("CHANNEL_OR_GROUP_ID", "-1001863324887"))
MESSAGE_ID = int(os.environ.get("MESSAGE_ID", "2"))
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS", "5545068262").split(' ')]

async def start_web_client():
    cheb = web.Application()
    cheb.router.add_get('/', hello_world)
    cheb.router.add_get('/get_streams', get_streams)
    cheb.router.add_get('/get_anime', get_anime)
    runner = web.AppRunner(cheb)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)  # Replace with your desired host and port
    await site.start()
    print("Web client started")
    await app.run(main_teletips())    
    await asyncio.create_task(store_streams())
    await asyncio.create_task(hen_videoss())


async def hen_videoss():
       while not await asyncio.sleep(3600):
           await store_streams()
           asyncio.create_task(hen_videoss())
           break
       asyncio.create_task(hen_videoss())

        
async def store_streams():
      cursor = streamdb.find({})
      async for document in cursor:
        title = document.get('title')
        episode = document.get('episode')
        streams = document.get('streams')
        key = (str(title), int(episode))
        if key not in data_dict:
            data_dict[key] = streams

async def hello_world(request):
    return web.Response(text='cheems')

async def get_streams(request):
    title = request.rel_url.query.get('name', '')
    episode = request.rel_url.query.get('ep', '')
    episode = 1 if episode is None else int(episode)
    if not title:
        return web.json_response({'error': 'Title and episode are required.'}, status=400)
    try:
        stream_data = animdl_grab(title, provider="haho", episode_number=episode)
        streams_info = stream_data["anime_data"][0]["streams"]
        streams = [{'url': stream_info['stream_url'], 'height': str(stream_info['quality'])} for stream_info in streams_info]
        return web.json_response(streams)
    except:
        return web.json_response({'error': 'Data not found for the provided title and episode.'}, status=404)

async def get_anime(request):
    title = request.rel_url.query.get('name', '')
    episode = request.rel_url.query.get('ep', '')
    episode = 1 if episode is None else int(episode)
    if not title:
        return web.json_response({'error': 'Title and episode are required.'}, status=400)
    try:
       stream_data = animdl_grab(title, provider="gogoanime", episode_number=episode)
       streams_info = stream_data["anime_data"][0]["streams"]
       streams = [{'stream_url': stream_info['stream_url']} for stream_info in streams_info]
       return web.json_response(streams)
    except:
        return web.json_response({'error': 'Data not found for the provided title and episode'}, status=404)
        
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
                        await asyncio.sleep(20)
                        zzz_teletips = await app.get_history(bot, limit = 1)
                        for ccc in zzz_teletips:
                            bbb = ccc.message_id
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
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y")
                last_upstat = time.strftime(f"%I:%M %p")
                xxx_teletips += f"\n\n**--Last checked on:--**\nDate: {last_update}\nTime: {last_upstat} IST</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(600)

async def run_app():
    await start_web_client()

if __name__ == "__main__":
    asyncio.run(run_app())
