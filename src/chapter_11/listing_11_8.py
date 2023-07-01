import asyncio
from asyncio import Semaphore


async def acquire(semaphore: Semaphore):
    print("Ожидание возможности захвата")
    async with semaphore:
        print("Захвачен")
        await asyncio.sleep(5)
    print("Освобождается")


async def release(semaphore: Semaphore):
    print("Одиночное освобождение!")
    semaphore.release()
    print("Одиночное освобождение - готово!")


async def main():

    semaphore = Semaphore(2)

    print("Два захвата, три освобождения...")
    await asyncio.gather(acquire(semaphore), acquire(semaphore), release(semaphore))

    print("Три захвата...")
    await asyncio.gather(acquire(semaphore), acquire(semaphore), acquire(semaphore))


asyncio.run(main())
