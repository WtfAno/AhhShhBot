import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from config import bot, START_PIC, START_MESSAGE, START_BUTTONS

@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
   await message.reply_photo(
         photo = START_PIC,
         caption = START_MESSAGE,
         reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    )

bot.run()
