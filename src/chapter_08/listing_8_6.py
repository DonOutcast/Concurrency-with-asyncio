import asyncio
from src.util.delay_functions import delay
from listing_8_5 import create_stdin_reader


async def main():
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))

if __name__ == "__main__":
    asyncio.run(main())
