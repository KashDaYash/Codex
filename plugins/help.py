from config import * 
from bot import Client, dbot as bot
from pyrogram import filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from db import *

HELP_TEXT = f"😇How To use  m\npress /buy to purchase a subscription\nIndex a group with - /index \nEXAMPLE: /index -100xxxxxxxxxxx Add me in the channel. And make sure I have all the permissions!\n\nRemove a Channel with - /remove -100xxxxxxxxxxx\nthis will help you to remove a indexed channel from your group. Get indexed channels list with - /viewlist \nCheck your information with - /info\nGives your information and validity of your subscription\nGet ID of current chat - /id \nAuto delete : use /autodel command to enable or disable auto message delete system."


  
@Client.on_message(filters.command("help"))
async def help_handler(_, m):
  await m.reply(HELP_TEXT)

@Client.on_message(filters.command("buy")) 
async def buy_handle(_ ,m):
  BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="USD $$",callback_data="usd_pp"),
  InlineKeyboardButton(text="INR ₹₹",callback_data="inr_pp")
  ]])
  await m.reply(text="All The Available Plans",reply_markup=BUTTON)
  
@bot.on_callback_query()
async def cb_help(_, callback_query: q):
  data = q.data
  PLAN_USD = "These are the prices in USD:\n\n`1.5 USD` - per Month\n`5 USD` - per 6 Months\n8 USD` - per Year\n\nClick on the Buy button to contact the owner"
    
  PLAN_INR = "**These are the prices in INR:**\n\n`100 INR` - per Month\n`400 INR` -  per 6 Months\n`800 INR` -  per Year\n\nClick on the `Buy` button to contact the owner"

  BTN_1 = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="Buy",url=f"t.me/{OWNER}"),
  InlineKeyboardButton(text="INR PRICE",callback_data="inr_p")
  ]])
  BTN_2 = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="Buy",url=f"t.me/{OWNER}"),
  InlineKeyboardButton(text="USD PRICE",callback_data="usd_p")
  ]])
  if data == "inr_pp": 
    await q.message.edit(PLAN_INR,reply_markup=BTN_2)
  elif data == "usd_pp": 
    await q.message.edit(PLAN_USD,reply_markup=BTN_1)
  elif data == "inr_p": 
    await q.message.edit(PLAN_INR,reply_markup=BTN_2)
  elif data == "inr_p": 
    await q.message.edit(PLAN_INR,reply_markup=BTN_2)
    
@Client.on_message(filters.command("id"))
async def id_handle(_, m):
  chat_id = m.chat.id
  user = m.from_user
  MSG = f"This Chat ID : `{chat_id}`\n"
  
  if m.reply_to_message:
    user_id = m.reply_to_message.from_user.id
    MSG += f"Reply User ID: `{user_id}`"
  elif m.from_user:
    user_id = m.from_user.id
    MSG += f"Your ID: `{user_id}`"
  else:
    None
  
  await m.reply(MSG)