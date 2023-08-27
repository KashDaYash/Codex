from bot import Client
from config import OWNER 
from pyrogram import filters 

TEXT = f'''This bot is made by @{OWNER} A full time python developer

Our channel :- @movie_artss
Our selling channel :- @platimostore

Want to make any kind of bot & tool dm @{OWNER}'''

@Client.on_message(filters.command("about"))
async def about_handle(_,m):
  chat_id = m.chat.id
  await m.reply(TEXT)