from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *



@Client.on_message(filters.command("start") & filters.private & filters.group)
async def start_handle(_, m):
  user = m.from_user
  id = m.chat.id
  await add_user(id=user.id, name=user.username)
  START_MSG = f'''Hey {user.username}    
    
I am the first & best ever Filter Bot ! 
I will filter your channel posts automatically and send it in your group chat when someone needs it.

Press /help for more info!
Press /buy to purchase a subscription!

your chat id = {id}'''
  await m.reply(START_MSG)
  
  
  




