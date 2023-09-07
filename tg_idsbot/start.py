from data import Data
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
    print("/start")
    user = await bot.get_me()
    mention = getattr(user, "mention", None)
    await bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention, msg.from_user.id),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
