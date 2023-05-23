import asyncio
import aiohttp
from src.util.asyn_timer import async_timed
from src.chapter_04 import fetch_status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        url = 'https://www.google.ru'
        pending = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url))
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f"Число завершившихся задач: {len(done)}")
            print(f"Число ожидающих задач: {len(pending)}")

            for done_task in done:
                print(await done_task)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())