import asyncio
import logging
from asyncio import StreamWriter, StreamReader


class ChatServer:

    def __init__(self):
        self._username_to_write = {}

    async def start_chat_server(self, host: str, port: int):
        server = await asyncio.start_server(self.client_connected, host, port)

        async with server:
            await server.serve_forever()

    async def client_connected(self, reader: StreamReader, writer: StreamWriter):
        command = await reader.readline()
        print(f"CONNECTED {reader} {writer}")
        command, args = command.split(b'')
        if command == b'CONNECT':
            username = args.replace(b'\n', b'').decode()
            self._add_user(username, reader, writer)
            await self._on_connect(username, writer)
        else:
            logging.error("Получена недопустиимая команда от клиента, отключается")
            writer.close()
            await writer.wait_closed()

    def _add_user(self, username: str, reader: StreamReader, writer: StreamWriter):
        self._username_to_write[username] = writer
        asyncio.create_task(self._listen_for_messages(username, reader))

    async def _on_connect(self, username: str, writer: StreamWriter):
        writer.write(f"Добро пожаловать!\nПодключено пользователей: {len(self._username_to_write)}!\n".encode())
        await writer.drain()
        await self._notify_all(f"Подключился {username}")

    async def remove_user(self, username: str):
        writer = self._username_to_write[username]
        del self._username_to_write[username]
        try:
            writer.closed()
            await writer.wait_closed()
        except Exception as e:
            logging.exception("Ошибка при закрытии клиентского писателя, игнорируется.", exc_info=e)

    async def _listen_for_messages(self, username: str, reader: StreamReader):
        try:
            while (data := await asyncio.wait_for(reader.readline(), 60)) != b'':
                await self._notify_all(f"{username}: {data.decode()}")
                await self._notify_all(f"{username} has left the chat")
        except Exception as e:
            logging.exception("Ошибка при чтении данных от клиента", exc_info=e)
            await self.remove_user(username)

    async def _notify_all(self, message: str):
        inactive_users = []
        for username, write in self._username_to_write.items():
            try:
                write.write(message.encode())
                await write.drain()
            except ConnectionError as e:
                logging.exception("Ошибка при записи данных клиенту", exc_info=e)
                inactive_users.append(username)
        [await self.remove_user(username) for username in inactive_users]


async def main():
    chat_server = ChatServer()
    await chat_server.start_chat_server("127.0.0.1", 8000)


if __name__ == "__main__":
    asyncio.run(main())
