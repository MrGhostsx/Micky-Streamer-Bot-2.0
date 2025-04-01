from aiohttp import web
from .stream_routes import routes

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2
