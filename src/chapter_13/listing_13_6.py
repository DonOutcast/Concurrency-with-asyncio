import asyncio
from asyncio.subprocess import Process


async def main():
    program = ["python3", "listing_13_4.py"]
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)

    print(f"pid процесса: {process.pid}")

    stdout, stderr = await process.communicate()
    print(stdout)
    print(stderr)
    print(f"Процесс вернул: {process.returncode}")


asyncio.run(main())


