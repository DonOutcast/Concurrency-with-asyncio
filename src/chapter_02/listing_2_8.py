import asyncio
from src.util.delay_functions import delay


async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)


asyncio.run(main())
