from bot import yk as bot
from db import *
from config import *
from pyrogram import filters



@bot.on_message(filters.command("start"))
async def start_handle(_, m):
  user = m.from_user
  id = m.chat.id
  await add_user(id=user.id, name=user.username)
  START_MSG = f"Hey {user.mention}\nI am the first & best ever Filter Bot !\nI will filter your channel posts automatically and send it in your group chat when someone needs it.\n\nPress /help for more info!\nPress /buy to purchase a subscription!\n\nyour chat id = {id}"
  
  await m.reply(START_MSG)
  




