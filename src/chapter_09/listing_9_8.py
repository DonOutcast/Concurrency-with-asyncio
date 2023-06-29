import asyncpg
from asyncpg import Record
from asyncpg.pool import Pool
from typing import List, Dict
from starlette.routing import Route
from starlette.requests import Request
from starlette.applications import Starlette
from starlette.responses import Response, JSONResponse


async def create_database_pool():
    pool: Pool = await asyncpg.create_pool(
        host="127.0.0.1",
        port=5432,
        user="lymondgl",
        password="",
        database="products",
        min_size=6,
        max_size=6,
    )

    app.state.DB = pool


async def destroy_database():
    pool = app.state.DB
    await pool.close()


async def brands(request: Request) -> Response:
    connection: Pool = request.app.state.DB
    brand_query = """SELECT brand_id, brand_name FROM brand;"""
    results: List[Record] = await connection.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return JSONResponse(result_as_dict)


app = Starlette(
    routes=[Route("/brands", brands)],
    on_startup=[create_database_pool],
    on_shutdown=[destroy_database],
)
