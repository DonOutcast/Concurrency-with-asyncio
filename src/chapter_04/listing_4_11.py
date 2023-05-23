import aiohttp
import asyncio
import logging
from src.util.asyn_timer import async_timed
from src.chapter_04 import fetch_status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://www.google.ru')
        bad_request = fetch_status(session, 'https://www.google.u')

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request)
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
