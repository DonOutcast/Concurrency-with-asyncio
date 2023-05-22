import asyncio
from src.util.delay_functions import delay


async def main() -> None:
    results = await asyncio.gather(delay(3), delay(1))
    print(results)

asyncio.run(main())
