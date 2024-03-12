import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @LOVELYR_OBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6154979500))

bot = Client('myacc', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
START_PIC = 'https://graph.org/file/f7da95a365c0f89c85fb7.jpg'
START_MESSAGE = """**ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ꜱᴀᴠᴇ ꜱᴇᴄʀᴇᴛ ᴘɪᴄꜱ ᴀɴᴅ ᴠɪᴅᴇᴏꜱ ꜱᴇɴᴛ ᴡɪᴛʜ ᴛɪᴍᴍᴇʀ** \n\n**ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ**\n\n**ᴛʜᴀɴᴋ ʏᴏᴜ!!!**"""
START_BUTTONS = [
    [
        InlineKeyboardButton('𝘜𝘱𝘥𝘢𝘵𝘦𝘴', url='https://t.me/BotsDom')
    ]
]
