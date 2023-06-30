import functools
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from listing_10_4 import DB_KEY, create_database_pool, destroy_database_pool

routes = web.RouteTableDef()

@routes.get("/users/{id}/cart")
async def time(request: Request) -> Response:
    try:
        str_id = request.match_info["id"]
        user_id = int(str_id)
        db = request.app["DB_KEY"]
        cart_query = """SELECT product_id FROM user_cart WHERE user_id = $1"""
        result = await db.fetch(cart_query, user_id)
        if result is not None:
            return web.json_response([dict(record) for record in result])
        else:
            raise web.HTTPNotFound()
    except ValueError:
        raise web.HTTPBadRequest()

app = web.Application()
app.on_startup.append(
    functools.partial(
        create_database_pool,
        host="127.0.0.1",
        port=5432,
        user="lymondgl",
        password="",
        database="cart",
    )
)

app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app, port=8003)
