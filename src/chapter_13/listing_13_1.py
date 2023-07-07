import asyncio
from asyncio.subprocess import Process


async def main():
    process: Process = await asyncio.create_subprocess_exec("ls", "-l")
    print(f"pid процесса: {process.pid}")
    status_code = await process.wait()
    print(f"Код состояния: {status_code}")


if __name__ == "__main__":
    asyncio.run(main())
