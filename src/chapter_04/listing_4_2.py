import asyncio
import aiohttp
from aiohttp import ClientSession
from src.util.asyn_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        url = "https://www.google.ru"
        status = await fetch_status(session, url)
        print(f"Состояние для {url} было равно {status}")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
