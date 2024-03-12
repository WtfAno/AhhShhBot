import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from config import START_PIC, START_MESSAGE, START_BUTTONS

bot = Client('myacc', api_id='10534530', api_hash='8760d7849212237231adda6255eec300', bot_token='7102962242:AAH4X4bRWt9176cyzgPEvxYmJfyk6Zg88do')

@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
   await message.reply_photo(
         photo = START_PIC,
         caption = START_MESSAGE,
         reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    )

bot.run()
