import asyncio
import aiohttp
from src.util.asyn_timer import async_timed
from src.chapter_04 import fetch_status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        url = 'https://www.google.ru'
        api_a = fetch_status(session, url)
        api_b = fetch_status(session, url, 2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending:
            if task is api_b:
                print("API B слишком медленный, отмена")
                task.cancel()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
