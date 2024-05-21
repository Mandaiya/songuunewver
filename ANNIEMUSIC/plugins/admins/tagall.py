from ANNIEMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " yunnaku lam yen da intha velai - venna thalaiya🥱 ",
           " yunaku irrukura LIFE ha yennaku donate pannidu apo than neku santhosam ",
           " Vc la yentha ponnu kitta urutitu irrukaa👻🙊 ",
           " summa thane irruka antha TV remote yedhutu kudu da manga manda 😁🥲 ",
           " mooku kila vai irruku athuku mela yenna irruku - romba yosikatha yenna moolaiye illala 🤣🤣 ",
           " athu yenna nu therla athu yeppadey solurathu nu therla - yunna partha paitiyam marri irruku 😁 ",
           " nan yarru yunakku nee yar yennaku ?? ",
           " nalla saptiya apo nalla toongu - illana mokka potutu irrupa  ",
           " Oree kulu kulu nu irrukiyoo inga va yevalo sooda irruku nu parru ",
           " Ivana yedhu vechi adikulam",
           " yenna da guru guru nu pakuraa - Deii  ",
           " yenga irrunthu da varenga yenaku neh  ",
           " sari nan poi velaiye pakuren - varaaataahhh ",
           " suthuthey suthuthey boombi - nee yenna vitu ponna pothumada saami 🤣🤣 ",
           " konjam kanda thna irrukum adjust paniko illana palahidum ",
           " dei Kundu yunaku yenna da velai inga ",
           " aasaiya kekuren - Saptiya - cut - shot nalla vanthuchi Thank you 🤔 ",
           " Hi Hello Hey Vanakam Vanthanam - poitu varen ",
           " pesuran pesuran Vc la ana avan yenna sonnalum yennku tookam varalaiye 😅 ",
           " dei nee lam vantha yenna varaliyana yenna - poi velaiya paru daw 🫣 ",
           " saptiya nee - 1 ",
           " yenna soru thina - 2 ",
           " yennaku kodukama sapudura nee lam nalla irrupa - 3 ",
           " sari nalla toongitu work parru  - 20 ",
           " dei last bench kara toongatha da 😮‍💨 - 4 ",
           " nalla saptu saptu toonguran pare 😬 - 5 ",
           " ipo nee yelunthukula nu vei 🫣 - 8 ",
           " Yun left side la parru un crush irrukanga - 9 ",
           " sari toongu kanavula un crush varum 😝😅 - 10 ",
           " nalla sapta pola inga varikum kekuthu yaepom 🙈😃 - 6 ",
           " dei nalavaneee yelunthudu da - 7 " ,
           " sari sari toongunathu pothum velaiya parru - 11 ",
           " innoruka polam variya sorru thinga - 12 ",
           " sari oru tips solluren - toongama irruka - 13 ",
           " pakathula work la un crush irruntha.. manager ku theriyama sight adey 🤧 ",
           " sari sari parthathu pothum ipo parru nalla mandaila yerum 🫥 - 16 ",
           " ninachen , yenna da kannu vera yengaiyo poguthu nu  😂 - 17 ",
           " sari work pandra pasanga luku - meeting nu yulla poidunga 😃 - 18 ",
           " AC la semaiya toongalam 🙈 - 19 ",
           " Aaga inniku mudinzichi tipss hu ! Varaataahhhh 🏃‍♂️ - 21 ",
           ]

@app.on_message(filters.command(["tagall"], prefixes=["/","!"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐆𝐫𝐩 𝐥𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐩𝐨𝐝𝐮𝐧𝐠𝐚.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("ʏᴜɴɢᴀᴋᴜʟᴜ ᴀᴅᴍɪɴ ᴘᴏᴛᴀᴛʜᴜᴋᴜ ᴀᴘᴘᴀʀᴀᴍ ᴛʜᴀɴ ᴀᴄᴄᴇᴘᴛ ᴀᴀɢᴜᴍ . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("ʏᴜɴɢᴀᴋᴜʟᴜ ᴀᴅᴍɪɴ ᴘᴏᴛᴀᴛʜᴜᴋᴜ ᴀᴘᴘᴀʀᴀᴍ ᴛʜᴀɴ ᴀᴄᴄᴇᴘᴛ ᴀᴀɢᴜᴍ.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**𝙽𝚊𝚗𝚍𝚛𝚒𝚐𝚊𝚕 𝚞𝚜𝚎 𝚙𝚊𝚗𝚗𝚊𝚝𝚑𝚞𝚔𝚞🫠 meendum varga**")
