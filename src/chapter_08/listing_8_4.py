import asyncio
from src.util.delay_functions import delay


async def main():
    while True:
        delay_time = input("Введите время сна: ")
        asyncio.create_task(delay(int(delay_time)))


if __name__ == "__main__":
    asyncio.run(main())

