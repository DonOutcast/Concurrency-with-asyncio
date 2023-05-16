import asyncio
from listing_2_16 import async_timed

@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"Засыпаю на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"Сон в течении {delay_seconds}")
    return delay_seconds

@async_timed()
async def main() -> None:
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

if __name__ == "__main__":
    asyncio.run(main())

