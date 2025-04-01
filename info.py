import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

# Bot information
SESSION = environ.get('SESSION', 'Webtsbot')
API_ID = int(environ.get('API_ID', '12345678'))
API_HASH = environ.get('API_HASH', '1234569874589632541')
BOT_TOKEN = environ.get('BOT_TOKEN', "7091568:AAABGRES4586965ERSTVS")
BOT_USERNAME = environ.get("BOT_USERNAME", 'SnapLinkMasterBot') # without @ 

# Admins, Channels & Users
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-100')) # admin your channel in stream 
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-100')) # admin your channel in users log 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6910445402').split()] # 3567788, 678899, 5889467
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'BOT_OWNER26') # without @ 

# pics information
PICS = environ.get('PICS', 'https://i.ibb.co/vvRqnDrZ/Uploaded-6910445402.jpg')

# channel link information
CHANNEL = environ.get('CHANNEL', 'https://t.me/Tech_Shreyansh')
SUPPORT = environ.get('SUPPORT', 'https://t.me/MrGhostsx2')

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

# file limit information
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", False) # True and False
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", "600"))  # limit time 600 = 10 minutes 
MAX_FILES = int(environ.get("MAX_FILES", "10"))  # file limit 10 file Olay

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

# ban information
BANNED_CHANNELS = [int(banned_channels) if id_pattern.search(banned_channels) else banned_channels for banned_channels in environ.get('BANNED_CHANNELS', '').split()]   
BAN_CHNL = [int(ban_chal) if id_pattern.search(ban_chal) else ban_chal for ban_chal in environ.get('BAN_CHNL', '').split()]
BAN_ALERT = environ.get('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ [ᴍʀ ɢʜᴏꜱᴛ](https://telegram.me/SmartEdith_Bot) ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>')

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://")
DATABASE_NAME = environ.get('DATABASE_NAME', "MrGhostsx")

# fsub  information
AUTH_PICS = environ.get('AUTH_PICS', 'https://i.ibb.co/vvRqnDrZ/Uploaded-6910445402.jpg')              
AUTH_CHANNEL = (environ.get("AUTH_CHANNEL", "-100"))
FSUB = environ.get("FSUB", True)

# port information
PORT = int(getenv('PORT', '2626'))
NO_PORT = bool(getenv('NO_PORT', False))

#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2

# time information
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

# Online Stream and Download
BIND_ADDRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
WORKERS = int(getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(environ.get('name', 'mrghostsbot'))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
else:
    ON_HEROKU = False
FQDN = str(getenv('FQDN', BIND_ADDRESS)) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}{}/".format(FQDN, "" if NO_PORT else ":" + str(PORT))
      
#Dont Remove My Credit @MrGhostsx
#This Repo Is By @Tech_Shreyansh 
# For Any Kind Of Error Ask Us In Support Group @MrGhostsx2
