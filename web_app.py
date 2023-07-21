from animdl.core.cli.commands.grab import animdl_grab
from aiohttp import web
import asyncio
import json
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

data_dict = {}
mongo = MongoClient("mongodb+srv://sneha:sneha@cluster0.zhphhyu.mongodb.net/?retryWrites=true&w=majority")
db = mongo.cheemsnsfk
streamdb = db.animestream

async def start_web_client():
    app = web.Application()
    app.router.add_get('/', hello_world)
    app.router.add_get('/get_streams', get_streams)
    app.router.add_get('/get_anime', get_anime)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)  # Replace with your desired host and port
    await site.start()
    print("Web client started")
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
