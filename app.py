from animdl.core.cli.commands.grab import animdl_grab
from aiohttp import web
import json

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
