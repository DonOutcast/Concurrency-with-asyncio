import asyncio
from src.util.delay_functions import delay

def call_later() -> None:
    print("Меня вызовут в ближайщем будущем!")

async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main())