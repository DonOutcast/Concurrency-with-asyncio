import asyncio
from src.util.delay_functions import delay
from src.util.asyn_timer import async_timed


async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(1)
        yield integer


@async_timed()
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f"Получено число {number}")


asyncio.run(main())
