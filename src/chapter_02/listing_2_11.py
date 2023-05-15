import asyncio
from asyncio import CancelledError
from src.util.delay_functions import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print("Задача не закончилась, следующая проверка через секунду.")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print("Наша задача была снята")


asyncio.run(main())
