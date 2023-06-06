import asyncio
import asyncpg
from asyncpg.transaction import Transaction


async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        user="lymondgl",
        password="lymondgl",
        database="products",
    )

    transaction: Transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute("""INSERT INTO brand VALUES(DEFAULT, 'brand_1');""")
        await connection.execute("""INSERT INTO brand VALUES(DEFAULT, 'brand_2');""")
    except asyncpg.PostgresError:
        print("Ошибка, транзакция откатывается!")
        await transaction.rollback()
    else:
        print("Ошибки нет, транзакция фиксируется!")
        await transaction.commit()

    query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%';"""

    brands = await connection.fetch(query)
    print(brands)
    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
