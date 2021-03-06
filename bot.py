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
๐๐๐ฎ {},
๐ผ๐ข ๐๐ฉ๐๐๐ ๐๐ง ๐๐ ๐๐๐ฃ๐๐๐ง ๐ฝ๐ค๐ฉ. 
๐ ๐๐๐ฃ ๐๐๐ฃ๐ ๐'๐ ๐ค๐ ๐๐ฃ ๐จ๐ฉ๐๐๐ ๐๐ง. ๐๐ช๐จ๐ฉ ๐จ๐๐ฃ๐ ๐ข๐ ๐ ๐จ๐ฉ๐๐๐ ๐๐ง ๐ ๐ฌ๐ค๐ช๐ก๐ ๐ง๐๐ฅ๐ก๐ฎ ๐ฌ๐๐ฉ๐ ๐๐ฉ๐จ ๐'๐
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
        InlineKeyboardButton('๐คOwner', url='https://t.me/HydraLivegrambot'), 
        InlineKeyboardButton('CHANNEL๐ข', url=f"https://telegram.me/{Config.CHANNEL}")
        ]]
    )

@Bot.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"Your Requested Sticker's ID is   * `{message.sticker.file_id}` *", quote=True)
   
Bot.run()
