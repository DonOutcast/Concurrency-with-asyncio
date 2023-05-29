import asyncpg
import asyncio

async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        user="lymondgl",
        database="lymondgl",
        password=""
    )
    version = connection.get_server_version()
    print(f"Подключено! Версия Postgres равна {version}")
    await connection.close()

asyncio.run(main())

