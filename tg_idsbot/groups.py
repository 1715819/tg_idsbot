from pyrogram import Client, filters

# Groups Welcome
@Client.on_message(filters.new_chat_members)
async def welcome(bot, msg):
    bot_id = bot.id
    if msg.new_chat_members[0].id == bot_id:
        await msg.reply(
            f"Thanks for adding me here! \n\nThis Group's ID is `{msg.chat.id}`"
        )
    else:
        pass
