from pyrogram import Client, filters

@Client.on_message(filters.private & filters.forwarded)
async def forwarded(bot, msg):
    text = ""
    
    if msg.forward_from:
        text += "Forward detected!\n\n"
        
        if msg.forward_from.is_bot:
            text += "**Bot**"
        else:
            text += "**User**"
            
        text += f'\n{msg.forward_from.first_name}\n'
        
        if msg.forward_from.username:
            text += f'@{msg.forward_from.username}\nID : `{msg.forward_from.id}`'
        else:
            text += f'ID : `{msg.forward_from.id}`'
    else:
        if msg.forward_sender_name:
            text += f"Forward detected but unfortunately, {msg.forward_sender_name} has enabled forwarding privacy, so I can't get their id"
        else:
            text += "Forward Detected.\n\n"
            
            chat_type = getattr(msg, "forward_from_chat", None)
            
            if chat_type and hasattr(chat_type, "type") and chat_type.type:
                if chat_type.type == "channel":
                    text += "**Channel**"
                elif chat_type.type == "supergroup":
                    text += "**Group**"
                    
                text += f'\n{chat_type.title}\n'
                
                if chat_type.username:
                    text += f'@{chat_type.username}\n'
                text += f'ID : `{chat_type.id}`'
    
    await msg.reply(text, quote=True)
