from pyrogram.types import Message, filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery

import config

bot = Client('myacc',
             api_id=config.API_ID,
             api_hash=config.API_HASH,
             bot_token=config.BOT_TOKEN)
X = -1002076462595
START_PIC = 'https://graph.org/file/f7da95a365c0f89c85fb7.jpg'
START_MESSAGE = """**ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ꜱᴀᴠᴇ ꜱᴇᴄʀᴇᴛ ᴘɪᴄꜱ ᴀɴᴅ ᴠɪᴅᴇᴏꜱ ꜱᴇɴᴛ ᴡɪᴛʜ ᴛɪᴍᴍᴇʀ** \n\n**ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ**\n\n**ᴛʜᴀɴᴋ ʏᴏᴜ!!!**"""
START_BUTTONS = [
    [
        InlineKeyboardButton('𝘜𝘱𝘥𝘢𝘵𝘦𝘴', url='https://t.me/BotsDom')
    ]
]
@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
    bot.send_photo(
        chat_id = X
        photo = START_PIC,
        caption = START_MESSAGE,
        reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    )
bot.run()
