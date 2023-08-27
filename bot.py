import logging
from datetime import datetime
import asyncio
from config import *
from pyrogram import *
from pyrogram.types import *

ADMIN = 1791227679

# Initialize logging
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"),
              logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger(__name__)

# Initialize clients
YaaraOP = Client(name="user", session_string=SESSION)
dbot = Client("testbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

class Bot(Client):
    def __init__(self):
        super().__init__("bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})

async def start(self):
  await super().start()
  YaaraOP.start()
  YaaraOP.send_message("me","STARTED")# Start the User client
  LOGGER.info("Bot Started ⚡")

async def stop(self): 
  await super().stop()
  await YaaraOP.stop()
  print("Bot Stopped 🚫")
  LOGGER.exception("Error while starting bot: %s", str(e))
