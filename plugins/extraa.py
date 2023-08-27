from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *



@Client.on_message(filters.command("info"))
async def info_handle(_, m):
  chat_id = m.chat.id
  id = m.from_user.id
  name = m.from_user.mention
  plan = ""
  if chat_id.startswith("-100"):
    plan += await get_group(chat_id)
  if m.chat.type == enums.ChatType.PRIVATE:
    if plan != "":
      await m.reply(f"Your Subscription Validity {plan}")
    else:
      await m.reply("You Are A Normal User\If You want to purchase use /buy")
    
  else:
    if plan != "":
      await m.reply(f"Hey {name} This Chat Plan Validity {plan}")
    else:
      BUTTON = InlineKeyboardMarkup([[
            InlineKeyboardButton("Buy A Plan", user_id=OWNER_ID)]])
      await m.reply(text=f"Hey {name} You Didn't Purchase Any Plan",reply_markup=BUTTON)
  
  
@Client.on_message(filters.command('leave') & filters.private &  filters.chat(OWNER_ID))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{OWNER}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Hello Friends, \nMy admin has told me to leave from group so i go! If you wanna add me again contact my support group.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"left the chat `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')
        
