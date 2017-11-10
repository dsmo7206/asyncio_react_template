#!/usr/bin/env python3

import asyncio
import uvloop

# uvloop is a faster drop-in replacement for the asyncio event loop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

import aiohttp_jinja2
import jinja2
from aiohttp import web as aiohttp_web

@aiohttp_jinja2.template('index.html')
def handle_root(request):
    print('Got root request %s' % request)
    return {'page_title': 'Test Title!'}

async def handle_hello(request):
    print('Got hello request %s' % request)
    name = request.match_info.get('name', 'Anonymous')
    return aiohttp_web.Response(text=('Hello, %s' % name))

async def handle_websocket(request):
    print('Got ws request %s' % request)
    ws = aiohttp_web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws closed with exception %s' % ws.exception())
    print('ws closed')
    return ws

def make_app():
    app = aiohttp_web.Application()

    # All aiohttp_jinja2 decorators will look in the given folder
    # when searching for html files
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('../client'))
    
    # All references to app.router.static in html templates
    # will point to the given directory.
    app.router.add_static('/static', '../client', name='static', append_version=True)
    
    # All GETs, POSTs, etc go here
    app.router.add_get('/', handle_root)
    app.router.add_get('/hello/{name}', handle_hello)
    app.router.add_get('/ws', handle_websocket)

    return app

def main():
    aiohttp_web.run_app(make_app())

if __name__ == '__main__':
    main()
