import aiohttp
import asyncio
import logging
from src.chapter_04 import fetch_status
from src.util.asyn_timer import async_timed

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'python://bat.ru')),
            asyncio.create_task(fetch_status(session, 'https://www.google.ru')),
            asyncio.create_task(fetch_status(session, 'https://www.google.ru'))
        ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающиз задач: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.all_tasks()

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())