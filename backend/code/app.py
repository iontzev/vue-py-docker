from aiohttp import web
import aioreloader

async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.get('/', hello)])

aioreloader.start()

web.run_app(app, port=80)