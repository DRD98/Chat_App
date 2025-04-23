from sanic import Sanic
from sanic.response import text


app = Sanic("ChatApp")

@app.get("/")
async def hello_world(request):
    return text("Hello Aeroplane")

@app.before_server_start
async def attach_db(app, loop):
    # app.ctx.db = Database()
    pass

