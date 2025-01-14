from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from config import Config
from data import Data

# 创建Pyrogram客户端
app = Client("my_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

# 回调函数
@app.on_callback_query()
async def _calls(bot, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    # .lower() to test somethings..
    if callback_query.data.lower() == "home":
        user = await bot.get_me()
        mention = user.mention
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.START.format(
                callback_query.from_user.mention, mention, callback_query.from_user.id
            ),
            reply_markup=InlineKeyboardMarkup(Data.buttons),
        )
    if callback_query.data.lower() == "about":
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_button),
        )

    if callback_query.data.lower() == "source":
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.SOURCE,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_button),
        )
    if callback_query.data.lower() == "help":
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_button),
        )
    """ More Plans """

# 启动Bot
if __name__ == "__main__":
    app.run()
