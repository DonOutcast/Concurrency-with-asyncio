import asyncio
from asyncio import StreamReader
from typing import AsyncGenerator


async def read_until_empty(stream_reader: StreamReader) -> AsyncGenerator[str, None]:
    while response := await stream_reader.readline():
        yield response.decode()


async def main():
    host: str = "www.example.com"

    request = f"GET / HTTP/1.1\r\n" \
              f"Connection: close\r\n" \
              f"Host: {host}\r\n\r\n"

    stream_reader, stream_writer = await asyncio.open_connection(host, 80)
    try:
        stream_writer.write(request.encode())
        await stream_writer.drain()

        responses = [response async for response in read_until_empty(stream_reader)]

        print("".join(responses))

    finally:
        stream_writer.close()
        await stream_writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())

