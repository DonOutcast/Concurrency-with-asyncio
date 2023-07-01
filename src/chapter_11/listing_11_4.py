import asyncio
from asyncio import Lock
from src.util.delay_functions import delay


async def a(lock: Lock):
    print("Сопраграмма а ждет возможности захватить блокировку")
    async with lock:
        print("Сопрограмма а находится в критической секции")
        await delay(2)
    print("Сопрограмма а освободила блокировку")


async def b(lock: Lock):
    print("Сопрограмма b ждет возможности захватить блокировку")
    async with lock:
        print("Сопрограмма b находится в критической секци")
        await delay(2)
    print("Сопрограмма b освободила блокировку")


async def main():
    lock = Lock()
    await asyncio.gather(a(lock), b(lock))


if __name__ == "__main__":
    asyncio.run(main())
