import asyncio
import logging
import asyncpg


async def main():
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="lymondgl",
        password="lymondgl",
        database="products",
    )
    try:
        async with connection.transaction():
            insert_brand = """INSERT INTO brand VALUES(9999, 'big_brand);'"""
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        logging.exception('Ошибка при выполнении транзакции')
    finally:
        query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'big_%';"""
        brands = await connection.fetch(query)
        print(f"Результат запроса: {brands}")

        await connection.close()

if __name__ == "__main__":
    asyncio.run(main())

