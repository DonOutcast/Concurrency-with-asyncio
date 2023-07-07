import asyncio
from asyncio import StreamReader
from asyncio.subprocess import Process


async def write_output(prefix: str, stdout: StreamReader):
    while line := await stdout.readline():
        print(f"[{prefix}]: {line.rstrip().decode()}")


async def main():
    program = ["ls", "-la"]
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)

    print(f"pid процесса: {process.pid}")
    stdout_task = asyncio.create_task(write_output(" ".join(program), process.stdout))

    return_code, _ = await asyncio.gather(process.wait(), stdout_task)
    print(f"Процесс вернул: {return_code}")


if __name__ == "__main__":
    asyncio.run(main())
