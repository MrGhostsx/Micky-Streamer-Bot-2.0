import os
import sys
import glob
import pytz
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle

# Credit headers remain the same
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

# Initialize paths and bot
ppath = "plugins/*.py"
files = glob.glob(ppath)
Webtsbot.start()

# Create new event loop properly
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

async def start():
    print('\n')
    print('Initializing Your Bot')
    bot_info = await Webtsbot.get_me()
    await initialize_clients()
    
    # Load plugins
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

    # Bot information setup
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    
    me = await Webtsbot.get_me()
    temp.BOT = Webtsbot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    
    # Time setup
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    
    # Notification messages
    await Webtsbot.send_message(LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    await Webtsbot.send_message(ADMINS[0], text='<b>ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ !!</b>')
    
    # Web server setup with proper error handling
    try:
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        site = web.TCPSite(app, bind_address, PORT)
        await site.start()
        print(f"Web server started on port {PORT}")
        
        # Run until stopped
        await idle()
        
    except Exception as e:
        logging.error(f"Web server error: {e}")
    finally:
        await app.cleanup()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')
    except Exception as e:
        logging.error(f"Fatal error: {e}")
    finally:
        loop.close()
