import asyncio
from asyncio import Queue, PriorityQueue
from typing import Tuple


async def worker(queue: Queue):
    while not queue.empty():
        work_item: Tuple[int, str] = await queue.get()
        print(f"Обрабатывается элемент {work_item}")
        queue.task_done()


async def main():
    priority_queue = PriorityQueue()
    work_items = [
        (3, "Lower priority"),
        (2, "Medium priority"),
        (1, "High priority"),
    ]

    worker_task = asyncio.create_task(worker(priority_queue))

    for work in work_items:
        priority_queue.put_nowait(work)

    await asyncio.gather(priority_queue.join(), worker_task)


if __name__ == "__main__":
    asyncio.run(main())
