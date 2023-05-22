import asyncio
from src.util.asyn_timer import async_timed
from src.util.delay_functions import delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

asyncio.run(main())
