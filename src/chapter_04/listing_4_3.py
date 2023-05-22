import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=1)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main() -> None:
    session_timeout = aiohttp.ClientTimeout(total=5, connect=1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, "https://www.google.ru")

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
