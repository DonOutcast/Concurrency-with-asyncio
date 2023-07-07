import asyncio
from asyncio.subprocess import Process


async def main():
    program = ["python3", "listing_13_4.py"]
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)

    print(f"pid  процесса: {process.pid}")

    return_code = await process.wait()
    print(f"Процесс вернул: {return_code}")


if __name__ == "__main__":
    asyncio.run(main())

