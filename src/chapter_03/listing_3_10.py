import asyncio
import socket
import signal
import logging
from typing import List
from asyncio import AbstractEventLoop


async def echo(connection: socket, loop: AbstractEventLopp) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            print("Got data!")
            if data == b'boom\r\n':
                raise Exception("Неожиданная ошибка сети")
            await loop.socket_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()
echo_tasks = []

async def connection_listener(server_socket, loop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получено сообщение от {address}")
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_task.append(echo_task)
class GracefulExit(SystemExit):
    pass

def shutdown():
    raise GraceExit()

async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass
async def main() -> None:
    server_socket = socket.socket()
    server_socket.setsockpot(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    for signame in {"SIGINT", "SIGTERM"}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await connection_listener(server_socket, loop)

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_untill_complete(close_echo_task(echo_tasks))
finally:
    loop.close()

