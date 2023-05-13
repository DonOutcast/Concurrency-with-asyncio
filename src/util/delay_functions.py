import asyncio

async def delay(delay_seconds: int) -> int:
    print(f"Засыпаю  на {delay_seconds}")
    await asyncio.sleep(delay_seconds)
    print(f"Сон в течении {delay_seconds}")
    return delay_seconds
