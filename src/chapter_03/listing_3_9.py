import asyncio, signal
from asyncio import AbstractEventLoop
from typing import Set

from src.util.delay_functions import delay

def cancel_tasks():
    print("Получен сигнал SIGINT!")
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f"Снимается {len(tasks)} задач.")
    [task.cancel() for task in tasks]

async def main() -> None:
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SGINT, cancel_tasks)

    await delay(10)

asyncio.run(main())



