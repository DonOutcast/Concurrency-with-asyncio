import time
import string
import random
import asyncio
from asyncio.subprocess import Process


async def encrypt(text: str) -> bytes:
    program = ["gpg", "-x", "--batch", "--passphrase", "3ncryptm3", "--cipher-algo", "TWOFISH"]

    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE,
                                                            stdin=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate(text.encode())
    return stdout


async def main():
    text_list = ["".join(random.choice(string.ascii_letters) for _ in range(1000)) for _ in range(100)]

    s = time.time()
    tasks = [asyncio.create_task(encrypt(text)) for text in text_list]
    encrypted_text = await asyncio.gather(*tasks)
    e = time.time()

    print(f"Время работы: {e - s}")
    print(encrypted_text)


if __name__ == "__main__":
    asyncio.run(main())
