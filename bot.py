import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

Bot = Client(
    "StickerIdBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
 
   
START_TEXT = """
𝙃𝙚𝙮 {},
𝘼𝙢 𝙎𝙩𝙞𝙘𝙠𝙚𝙧 𝙞𝙙 𝙁𝙞𝙣𝙙𝙚𝙧 𝘽𝙤𝙩. 
𝙄 𝙘𝙖𝙣 𝙁𝙞𝙣𝙙 𝙄'𝙙 𝙤𝙛 𝙖𝙣 𝙨𝙩𝙞𝙘𝙠𝙚𝙧. 𝙅𝙪𝙨𝙩 𝙨𝙚𝙣𝙙 𝙢𝙚 𝙖 𝙨𝙩𝙞𝙘𝙠𝙚𝙧 𝙄 𝙬𝙤𝙪𝙡𝙙 𝙧𝙚𝙥𝙡𝙮 𝙬𝙞𝙩𝙝 𝙞𝙩𝙨 𝙄'𝙙
"""
    
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👤Owner', url='https://t.me/HydraLivegrambot'), 
        InlineKeyboardButton('CHANNEL📢', url=f"https://telegram.me/{Config.CHANNEL}")
        ]]
    )

@Bot.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"Your Requested Sticker's ID is   * `{message.sticker.file_id}` *", quote=True)
   
Bot.run()
