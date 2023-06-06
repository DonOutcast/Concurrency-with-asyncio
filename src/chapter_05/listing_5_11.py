import asyncio
import asyncpg
import logging


async def main():
    connection = await asyncpg.connect(
        host="127.0.0.1",
        user="lymondgl",
        password="lymondgl",
        database="products",
    )

    async with connection.transaction():
        await connection.execute("""INSERT INTO brand VALUES(DEFAULT, 'my_new_brand');""")
        try:
            async with connection.transaction():
                await connection.execute("""INSERT INTO product_color VALUES(1, 'black');""")
        except Exception as ex:
            logging.warning("Ошибка при вставке цвета товара игнорируется", exc_info=ex)
        await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
