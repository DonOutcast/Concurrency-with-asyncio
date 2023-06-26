import asyncio
import logging
from asyncio import StreamReader, StreamWriter


class ServerState:

    def __init__(self):
        self._writers = []

    async def add_client(self, reader: StreamReader, writer: StreamWriter):
        self._writers.append(writer)
        await self._on_connect(writer)
        asyncio.create_task(self._echo(reader, writer))

    async def _on_connect(self, writer: StreamWriter):
        writer.write(f"Добро пожаловать! Число подключенных пользователй: {len(self._writers)}\n".encode())
        await writer.drain()
        await self._notify_all("Подключиля новый пользователь!\n")

    async def _echo(self, reader: StreamReader, writer: StreamWriter):
        try:
            while (data := await reader.readline()) != b'':
                writer.write(data)
                await writer.drain()
            self._writers.remove(writer)
            await self._notify_all(f"Клиент отключился. Осталось пользователей: {len(self._writers)}!\n")
        except Exception as e:
            logging.exception("Ошибка чтения данных от клиента", exc_info=e)
            self._writers.remove(writer)

    async def _notify_all(self, message: str):
        for write in self._writers:
            try:
                write.write(message.encode())
                await write.drain()
            except ConnectionError as e:
                logging.exception("Ошибка записи данных клиенту", exc_info=e)
                self._writers.remove(write)


async def main():
    server_state = ServerState()

    async def client_connected(reader: StreamReader, writer: StreamWriter) -> None:
        await server_state.add_client(reader, writer)

    server = await asyncio.start_server(client_connected, "127.0.0.1", 8000)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
