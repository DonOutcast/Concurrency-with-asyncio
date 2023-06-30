import asyncio
from listing_10_9 import retry, TooManyRetries


async def main():
    async def always_fail():
        raise Exception("А я грохнулась!")

    async def always_timeout():
        await asyncio.sleep(1)

    try:
        await retry(
            always_fail,
            max_retries=3,
            timeout=.1,
            retry_interval=.1
        )
    except TooManyRetries:
        print("Слшиком много попыток!")
    try:
        await retry(
            always_timeout,
            max_retries=3,
            timeout=.1,
            retry_interval=.1
        )
    except TooManyRetries:
        print("Слишком много попыток!")


asyncio.run(main())

