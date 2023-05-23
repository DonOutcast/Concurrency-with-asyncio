import asyncio
import aiohttp
from src.chapter_04 import fetch_status
from src.util.asyn_timer import async_timed

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.google.ru', 1),
            fetch_status(session, 'https://www.google.ru', 10),
            fetch_status(session, 'https://www.google.ru', 10)
        ]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("Произошел тайм-аут!")

        for task in asyncio.tasks.all_tasks():
            print(task)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())


