import re
from pyrogram import filters
import random
from ANNIEMUSIC import app



######### GOOD NIGHT 
@app.on_message(filters.command(["oodnightu","oodu Nightu","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**𝙴𝚛𝚊𝚟𝚞 𝚄𝚛𝚊𝚔𝚊𝚖, {sender}!  yenna inga thaiya vitutu poiduviya nee 🤨. **")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**𝙴𝚛𝚊𝚟𝚞 𝚄𝚛𝚊𝚔𝚊𝚖...., {sender}! 𝚗𝚊𝚗 𝚃𝚘𝚘𝚗𝚐𝚊 𝙿𝚘𝚛𝚎𝚗 tata 🌙 {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgQAAx0Ce9_hCAACaEVlwn7HeZhgwyVfKHc3WUGC_447IAACLgwAAkQwKVPtub8VAR018x4E", # Sticker 1
        "CAACAgIAAxkBAAEMDKVmNhq5BtT09o49HNLePsgTTBFCVAAC7xAAAoYv2UptiAX3zd_1PzQE",      # Sticker 2
        "CAACAgUAAxkBAAEMDKtmNhsAAZ0e0duF440Yp0l2UpWvjnEAAm4CAAIFJYlUY-HGbU0jEPg0BA", # Sticker 3
        "CAACAgUAAxkBAAEMDK1mNhsYQ6af8F7aGmRgtEqR0lXsGgAC1gcAAk4uaVcV6vAxamncxTQE",
        "CAACAgEAAxkBAAEMDLFmNhuArSTReGya2vpkr8N_0PU6AQACsQIAAmnJIUQJoO-rBLvyszQE",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
        "🌙",
        "🌃",
        "🌠",
        
    ]
    return random.choice(emojis)
