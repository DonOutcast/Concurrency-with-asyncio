import asyncio
import requests
from src.util.asyn_timer import async_timed


@async_timed()
async def get_google_status() -> int:
    return requests.get("https://www.google.ru").status_code


@async_timed()
async def main() -> None:
    task_1 = asyncio.create_task(get_google_status())
    task_2 = asyncio.create_task(get_google_status())
    task_3 = asyncio.create_task(get_google_status())

    await task_1
    await task_2
    await task_3

if __name__ == "__main__":
    asyncio.run(main())


