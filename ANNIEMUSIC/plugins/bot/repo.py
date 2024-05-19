from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

start_txt = """**
▄︻デ( ฬєɭς๏๓є เภ Շ๏ Շђє ฬ๏гɭ๔ - [ 𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ ] )═══━一̵̡Ӝ̵̨Ʒ
 
 ➲ ᴡᴇ ᴀʀᴇ ᴛʜᴇ 𝐇YPEƦꜱ - ᴡᴇʟʟ ᴋɴᴏᴡɴ ɢᴜʏꜱ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ
 
 ➲ ωє єηgαgє тнє яєρσ є∂ιтιηg ωιтн αη υηιqυє-ηєѕѕ ✰
 
 ➲ 𝙍𝙪𝙣𝙣𝙞𝙣𝙜 𝙤𝙣 𝙃𝙚𝙧𝙤𝙠𝙪 𝙖𝙣𝙙 𝙑𝙋𝙎. 𝙈𝙤𝙧𝙚 𝙋𝙡𝙖𝙣𝙨 𝙔𝙚𝙩 𝙩𝙤 𝙘𝙤𝙢𝙚 ✰
 
 ➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/Team_Hypers_Networks"),
             InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Team_Hypers_Networks"),
             ],
     
             [
             InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url="https://t.me/OXY474_STORE"),
             ],
     
             [
             InlineKeyboardButton("❝𝐌𝐮𝐬𝐢𝐜 -𝐂𝐮𝐭𝐞 𝐆𝐢𝐫𝐥❞", url=f"https://t.me/Rose_milk_chat_bot"),            
             InlineKeyboardButton("︎❝𝐌𝐮𝐬𝐢𝐜 -𝐎𝐧𝐞 𝐋𝐨𝐯𝐞❞", url=f"https://t.me/Maya_Music_Bot"),
             ],
     
             [
             InlineKeyboardButton("❝𝐂𝐡𝐚𝐭_𝐁𝐨𝐭 -𝐇𝐨𝐧𝐞𝐲❞", url=f"https://t.me/HoneychatzBot"),
             InlineKeyboardButton("❝𝐌𝐮𝐬𝐢𝐜 -𝐑𝐚𝐚𝐠𝐚𝐯𝐚𝐯𝐢𝐛𝐞𝐬❞", url=f"https://t.me/raagaaxvibesbot"),
             ],
     
             [
             InlineKeyboardButton("𝐀𝐋𝐋 𝐁𝐎𝐓𝐒", url=f"https://t.me/TeamHyperNetworks"),
             InlineKeyboardButton("❝𝐌𝐮𝐬𝐢𝐜 -𝐒𝐡𝐢𝐧𝐨𝐛𝐢❞", url=f"https://t.me/ShinobuMusicBot"),
             ],
     
              [
              InlineKeyboardButton("𝐆𝐈𝐓𝐇𝐔𝐁 𝐏𝐑𝐎𝐅𝐈𝐋𝐄", url=f"https://github.com/"),
              InlineKeyboardButton("HYPER-NET♡︎", url=f"https://t.me/Team_Hypers_Networks"),
              ],
     
              [
              InlineKeyboardButton("❝𝐌𝐨𝐯𝐢𝐞𝐬 -𝐒𝐕𝐃|𝐇𝐲𝐩𝐞𝐫❞", url=f"https://t.me/Moviesvdnest_botN"),
              ],
       ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/75aae54314783b81f553c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
