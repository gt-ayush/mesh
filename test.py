# test_ws.py
import asyncio
import websockets
import json

async def test():
    uri = "ws://127.0.0.1:8000/ws/chat/"

    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"message": "Hello from test"}))
        response = await websocket.recv()
        print(response)

asyncio.run(test())

