import asyncio
import asyncpg
from listing_5_2 import (
    CREATE_BRAND_TABLE,
    CREATE_PRODUCT_TABLE,
    CREATE_PRODUCT_COLOR_TABLE,
    CREATE_PRODUCT_SIZE_TABLE,
    CREATE_SKU_TABLE,
    SIEZE_INSERT,
    COLOR_INSERT,
)


async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        user="lymondgl",
        database="products",
        password="lymondgl"
    )

    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIEZE_INSERT,
        COLOR_INSERT
    ]
    print("Делается база данных product...")
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print("База данных product сделана!")
    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())

