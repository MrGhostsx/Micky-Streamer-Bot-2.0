import os, sys, glob, pytz, asyncio, logging, importlib
from pathlib import Path
from pyrogram import idle

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)
 
from info import *
from typing import Union, Optional, AsyncGenerator
from Script import script 
from datetime import date, datetime 
from aiohttp import web
from web import web_server
from web.server import Webtsbot
from utils import temp, ping_server
from web.server.clients import initialize_clients

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

ppath = "plugins/*.py"
files = glob.glob(ppath)
Webtsbot.start()
loop = asyncio.get_event_loop()

async def start():
    print('\n')
    print('Initalizing Your Bot')
    bot_info = await Webtsbot.get_me()
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Imported => " + plugin_name)

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2
    
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    me = await Webtsbot.get_me()
    temp.BOT = Webtsbot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await Webtsbot.send_message(LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    await Webtsbot.send_message(ADMINS[0], text='<b>ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ !!</b>')
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
