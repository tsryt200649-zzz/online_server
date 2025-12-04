# server.py
import asyncio
import os
import websockets

PORT = int(os.environ.get("PORT", 10000))
connected = set()

async def handler(ws, path):
    connected.add(ws)
    print("Player connected")

    try:
        async for msg in ws:
            print("Received:", msg)
            # 受け取ったメッセージを全員に中継
            for c in connected:
                if c != ws:
                    await c.send(msg)
    except:
        pass
    finally:
        if ws in connected:
            connected.remove(ws)
        print("Player disconnected")

async def main():
    print(f"Server running on port {PORT}")
    async with websockets.serve(handler, "0.0.0.0", PORT):
        await asyncio.Future()  # 永遠に動かす

asyncio.run(main())
