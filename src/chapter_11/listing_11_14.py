import asyncio
from asyncio import Condition


async def do_work(condition: Condition):
    while True:
        print("Ожидаю блокировка условия...")
        async with condition:
            print("Блокировка захвачена, освобождаю и жду выполнения условия...")
            await condition.wait()
            print("Условие выполнено, вновь захватываю блокировку условия...")
            await asyncio.sleep(1)
        print("Работа закончена, блокировака освобождена...")


async def fire_event(condition: Condition):
    while True:
        await asyncio.sleep(5)
        print("Перед уведомление, захавтываю блокировку условия...")
        async with condition:
            print("Блокировка захвачена, уведомляю всех исполнителей.")
            condition.notify_all()
        print("Исполнители уведомлены, освобождаю блокировку.")


async def main():
    condition = Condition()

    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition), do_work(condition))


if __name__ == "__main__":
    asyncio.run(main())
