import asyncio
from src.util.delay_functions import delay


async def main() -> None:
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача заняла более 5с, скоро она закончится!")
        result = await task
        print(result)

asyncio.run(main())


