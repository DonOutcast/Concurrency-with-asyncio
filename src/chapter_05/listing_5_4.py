import asyncpg
import asyncio
from asyncpg import Record
from typing import List


async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        user="lymondgl",
        database="products",
        password="lymongl"
    )
    await connection.execute("""INSERT INTO brand VALUES (DEFAULT, 'Levis');""")
    await connection.execute("""INSERT INTO brand VALUES (DEFAULT, 'Seven')""")

    brand_query = """SELECT brand_id, brand_name FROM brand;"""
    results: List[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f"id: {brand['brand_id']}, name: {brand['brand_name']}")
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
