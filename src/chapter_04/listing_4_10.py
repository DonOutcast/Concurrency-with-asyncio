import asyncio
import aiohttp
from aiohttp import ClientSession
from src.util.asyn_timer import async_timed
from src.chapter_04 import fetch_status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://www.google.ru')),
            asyncio.create_task(fetch_status(session, 'https://www.google.ru'))
        ]
        done, pending = await asyncio.wait(fetchers)
        print(f"Число завершихся задач: {len(done)}")
        print(f"Число ожидающих задач {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
