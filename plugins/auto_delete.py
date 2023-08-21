from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *

t_text = "This Time Auto-Delete Is **OFF** Click On Button And Set **ON**"
f_text = "This Time Auto-Delete Is **ON** Click On Button And Set **OFF**"

T_BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton("ON",callback_data ="do_true")
  ]])
F_BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton("OFF",callback_data ="do_false")
  ]])
@Client.on_message(filters.command("autodel") & filters.group)
async def auto_del_handler(_, m):
  chat_id = m.chat.id
  group = await get_group(chat_id)
  auto_dele = group['auto_del']
  if auto_dele == False:
    await m.reply(t_text,reply_markup=T_BUTTON)
  elif auto_dele == True:
    await m.reply(f_text,reply_markup=F_BUTTON)
    
@Client.on_callback_query()
async def auto_del_cq(_, q):
  chat_id = q.message.chat.id
  data = q.data
  if data == "do_true":
    await update_group(id, {"auto_del": True})
    await q.message.edit("This Chat Auto Delete Message **ON**")
  elif data == "do_false": 
    await update_group(id, {"auto_del": False})
    await q.message.edit("This Chat Auto Delete Message **OFF**")