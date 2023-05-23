import asyncio
import aiohttp
from aiohttp import ClientSession
from src.util.asyn_timer import async_timed


async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.google.ru', 1),
            fetch_status(session, 'https://www.google.ru', 1),
            fetch_status(session, 'https://www.google.ru', 10)
        ]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
