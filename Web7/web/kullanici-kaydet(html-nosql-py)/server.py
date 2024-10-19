import os
import json
import asyncio
import websockets
from aiohttp import web

json_yolu = os.path.join('veri', 'veri.json')

async def veri_kaydet(data):
    with open(json_yolu, 'a') as json_dosya:
        json.dump(data, json_dosya)
        json_dosya.write('\n')

async def websocket_isleyici(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        await veri_kaydet(data)
        await websocket.send(f"Veri kaydedildi: {data}")

async def websocket_sunucusunu_baslat():
    async with websockets.serve(websocket_isleyici, 'localhost', 6789):
        await asyncio.Future()

async def http_sunucusunu_baslat():
    app = web.Application()
    app.router.add_static('/sablon', path='sablon', name='sablon')
    app.router.add_get('/', lambda request: web.FileResponse('sablon/index.html'))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 33334)
    await site.start()
    print("HTTP sunucusu http://localhost:33334 adresinde çalışıyor.")

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(
        websocket_sunucusunu_baslat(),
        http_sunucusunu_baslat()
    ))
    loop.run_forever()
