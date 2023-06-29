import asyncio
import typing

from starlette.websockets import WebSocket
from starlette.routing import WebSocketRoute
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint


class UserCounter(WebSocketEndpoint):
    encoding = "text"
    sockets = []

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        UserCounter.sockets.append(websocket)
        await self._send_count()

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        UserCounter.sockets.remove(websocket)
        await self._send_count()

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        pass

    async def _send_count(self):
        if len(UserCounter.sockets) > 0:
            count_str = str(len(UserCounter.sockets))
            task_to_socket = {
                asyncio.create_task(websocket.send_text(count_str)): websocket for websocket in UserCounter.sockets
            }
            done, pending = await asyncio.wait(task_to_socket)
            for task in done:
                if task.exception() is not None:
                    if task_to_socket[task] in UserCounter.sockets:
                        UserCounter.sockets.remove(task_to_socket[task])


app = Starlette(routes=[WebSocketRoute("/counter", UserCounter)])



