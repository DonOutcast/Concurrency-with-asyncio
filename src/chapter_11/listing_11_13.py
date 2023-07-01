import asyncio
from asyncio import Event
from contextlib import suppress


async def trigger_event_periodically(event: Event):
    while True:
        print("Активируется событие!")
        event.set()
        await asyncio.sleep(1)


async def do_work_on_event(event: Event):
    while True:
        print("Ожидаю события...")
        await event.wait()
        event.clear()
        print("Работаю!")
        await asyncio.sleep(5)
        print("Работа закончена!")


async def main():
    event = asyncio.Event()
    trigger = asyncio.wait_for(trigger_event_periodically(event), 5.0)

    with suppress(asyncio.TimeoutError):
        await asyncio.gather(do_work_on_event(event), do_work_on_event(event), trigger)


if __name__ == "__main__":
    asyncio.run(main())
