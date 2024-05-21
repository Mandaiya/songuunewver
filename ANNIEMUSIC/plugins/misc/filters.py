import re
from ANNIEMUSIC import app
from config import BOT_USERNAME
from ANNIEMUSIC.utils.jarvis_ban import admin_filler
from ANNIEMUSIC.mongo.fillersdb import *
from ANNIEMUSIC.utils.fillers_func import GetfillerMessage, get_text_reason, SendfillerMessage
from ANNIEMUSIC.utils.yumidb import user_admin
from pyrogram import fillers
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(fillers.command("filler") & admin_filler)
@user_admin
async def _filler(client, message):
    
    chat_id = message.chat.id 
    if (
        message.reply_to_message
        and not len(message.command) == 2
    ):
        await message.reply("You need to give the filler a name!")  
        return 
    
    filler_name, filler_reason = get_text_reason(message)
    if (
        message.reply_to_message
        and not len(message.command) >=2
    ):
        await message.reply("You need to give the filler some content!")
        return

    content, text, data_type = await GetfillerMessage(message)
    await add_filler_db(chat_id, filler_name=filler_name, content=content, text=text, data_type=data_type)
    await message.reply(
        f"Saved filler '`{filler_name}`'."
    )


@app.on_message(~fillers.bot & fillers.group, group=4)
async def fillerCheckker(client, message):
    if not message.text:
        return
    text = message.text
    chat_id = message.chat.id
    if (
        len(await get_fillers_list(chat_id)) == 0
    ):
        return

    ALL_fillerS = await get_fillers_list(chat_id)
    for filler_ in ALL_fillerS:
        
        if (
            message.command
            and message.command[0] == 'filler'
            and len(message.command) >= 2
            and message.command[1] ==  filler_
        ):
            return
            
        pattern = r"( |^|[^\w])" + re.escape(filler_) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            filler_name, content, text, data_type = await get_filler(chat_id, filler_)
            await SendfillerMessage(
                message=message,
                filler_name=filler_,
                content=content,
                text=text,
                data_type=data_type
            )

@app.on_message(fillers.command('fillers') & fillers.group)
async def _fillers(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title 
    if message.chat.type == 'private':
        chat_title = 'local'
    fillerS = await get_fillers_list(chat_id)
    
    if len(fillerS) == 0:
        await message.reply(
            f'No fillers in {chat_title}.'
        )
        return

    fillers_list = f'List of fillers in {chat_title}:\n'
    
    for filler_ in fillerS:
        fillers_list += f'- `{filler_}`\n'
    
    await message.reply(
        fillers_list
    )


@app.on_message(fillers.command('stopsvd') & admin_filler)
async def stopall(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title 
    user = await client.get_chat_member(chat_id,message.from_user.id)
    if not user.status == ChatMemberStatus.OWNER :
        return await message.reply_text("Only Owner Can Use This!!") 

    KEYBOARD = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='Delete all fillers', callback_data='custfillers_stopall')],
        [InlineKeyboardButton(text='Cancel', callback_data='custfillers_cancel')]]
    )

    await message.reply(
        text=(f'Are you sure you want to stop **ALL** fillers in {chat_title}? This action is irreversible.'),
        reply_markup=KEYBOARD
    )


@app.on_callback_query(fillers.regex("^custfillers_"))
async def stopall_callback(client, callback_query: CallbackQuery):  
    chat_id = callback_query.message.chat.id 
    query_data = callback_query.data.split('_')[1]  

    user = await client.get_chat_member(chat_id, callback_query.from_user.id)

    if not user.status == ChatMemberStatus.OWNER :
        return await callback_query.answer("Only Owner Can Use This!!") 
    
    if query_data == 'stopall':
        await stop_all_db(chat_id)
        await callback_query.edit_message_text(text="I've deleted all chat fillers.")
    
    elif query_data == 'cancel':
        await callback_query.edit_message_text(text='Cancelled.')



@app.on_message(fillers.command('stopfiller') & admin_filler)
@user_admin
async def stop(client, message):
    chat_id = message.chat.id
    if not (len(message.command) >= 2):
        await message.reply('Use Help To Know The Command Usage')
        return
    
    filler_name = message.command[1]
    if (filler_name not in await get_fillers_list(chat_id)):
        await message.reply("You haven't saved any fillers on this word yet!")
        return
    
    await stop_db(chat_id, filler_name)
    await message.reply(f"I've stopped `{filler_name}`.")
