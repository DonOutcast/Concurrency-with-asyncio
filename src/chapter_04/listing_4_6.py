import asyncio
import aiohttp
from src.chapter_04 import fetch_status
from src.util.asyn_timer import async_timed

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        urls = ["https://www.google.ru" for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())