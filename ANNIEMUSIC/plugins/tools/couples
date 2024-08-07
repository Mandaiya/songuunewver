import os
import random
from datetime import datetime
from telegraph import upload_file
from PIL import Image, ImageDraw
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

# BOT FILE NAME
from ANNIEMUSIC import app as app
from ANNIEMUSIC.mongo.couples_db import _get_image, get_couple

def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list

def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a

tomorrow = str(dt_tom())
today = str(dt()[0])

# List of GIF URLs
gifs = [
    "https://telegra.ph/file/96d3ce385c179480af3c7.mp4",
    "https://telegra.ph/file/6626ec9526be31e13e613.mp4",
    "https://telegra.ph/file/402f37120d08b88b07877.mp4",
    "https://telegra.ph/file/6a1e05c8d75a85c5713b6.mp4",
    "https://telegra.ph/file/0aa2dc0e5d0c6112db947.mp4",
    "https://telegra.ph/file/78755006bc11bf8507197.mp4",
    "https://telegra.ph/file/16e66c57cfa20366047ed.mp4",
    # Add more GIF URLs as needed
]

@app.on_message(filters.command("friends"))
async def ftest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("This command only works in groups.")
    try:
        msg = await message.reply_text("✅")
        # GET LIST OF USERS
        list_of_users = []

        async for i in app.get_chat_members(message.chat.id, limit=50):
            if not i.user.is_bot:
                list_of_users.append(i.user.id)

        c1_id = random.choice(list_of_users)
        c2_id = random.choice(list_of_users)
        while c1_id == c2_id:
            c1_id = random.choice(list_of_users)

        photo1 = (await app.get_chat(c1_id)).photo
        photo2 = (await app.get_chat(c2_id)).photo

        N1 = (await app.get_users(c1_id)).mention
        N2 = (await app.get_users(c2_id)).mention

        try:
            p1 = await app.download_media(photo1.big_file_id, file_name="pfp.png")
        except Exception:
            p1 = "ANNIEMUSIC/assets/upic.png"
        try:
            p2 = await app.download_media(photo2.big_file_id, file_name="pfp1.png")
        except Exception:
            p2 = "ANNIEMUSIC/assets/upic.png"

        img1 = Image.open(f"{p1}")
        img2 = Image.open(f"{p2}")

        img = Image.open("ANNIEMUSIC/assets/annie/ANNIECP.png")

        img1 = img1.resize((486,486))
        img2 = img2.resize((486,486))

        mask = Image.new('L', img1.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + img1.size, fill=255)

        mask1 = Image.new('L', img2.size, 0)
        draw = ImageDraw.Draw(mask1)
        draw.ellipse((0, 0) + img2.size, fill=255)

        img1.putalpha(mask)
        img2.putalpha(mask1)

        draw = ImageDraw.Draw(img)

        img.paste(img1, (410, 500), img1)
        img.paste(img2, (1395, 500), img2)

        img.save(f'test_{cid}.png')

        TXT = f"""
      **𝐓ᴏᴅᴀʏ's 𝐅ʀɪᴇɴᴅs 🎉 : 
           ɄⱤɄ₱₳Đ₳ ₥₳₮₳₦₲₳ 🙊 
     [HY]✧═════•❁♡︎❁•═════✧[PER]
           {N1} + {N2} = 😍
       (@@)✧════•❁♡︎❁•════✧(oo)
      𝐍ᴇxᴛ 𝐅ʀɪᴇɴᴅs 𝐖ɪʟʟ 𝐁ᴇ 
         𝐒ᴇʟᴇᴄᴛᴇᴅ 𝐎ɴ {tomorrow} !!
      一═デ︻ 𝗡αℓιкυ 𝙔єηηα ηυ 𝙋ααρσм ︻デ═一**
"""

        # Select and send a random GIF
        gif_url = random.choice(gifs)
        await message.reply_animation(gif_url, caption=TXT)
        await msg.delete()
        a = upload_file(f"test_{cid}.png")
        for x in a:
            img = "https://graph.org/" + x
            friends = {"c1_id": c1_id, "c2_id": c2_id}
            # await save_couple(cid, today, friends, img)

    except Exception as e:
        print(str(e))
    try:
        os.remove(f"./downloads/pfp1.png")
        os.remove(f"./downloads/pfp2.png")
        os.remove(f"test_{cid}.png")
    except Exception:
        pass

__mod__ = "FRIENDS"
__help__ = """
**» /friends** - Get Todays Friends Of The Group In Interactive View
"""
