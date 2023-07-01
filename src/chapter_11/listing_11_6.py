import asyncio
from asyncio import Semaphore


async def operation(semaphore: Semaphore):
    print("Жду возможности захватить семафор...")
    async with semaphore:
        print("Семафор захвачен!")
        await asyncio.sleep(2)
    print("Семафор освобожден!")


async def main():
    semaphore = Semaphore(2)
    await asyncio.gather(*[operation(semaphore) for _ in range(4)])


if __name__ == "__main__":
    asyncio.run(main())

