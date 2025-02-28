import re

import requests
from bs4 import BeautifulSoup
from pyrogram import filters

from ANNIEMUSIC import app


def get_video_title(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title.string


def extract_video_id(url):
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.match(regex, url)
    if match:
        return match.group(1)
    return None


@app.on_message(
    filters.command(["getthumb", "genthumb", "thumb", "thumbnail"], prefixes="/")
)
async def get_thumbnail_command(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴜʀʟ ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ɢᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ"
        )
    try:
        a = await message.reply_text("Processing...")
        url = message.text.split(" ")[1]
        video_id = extract_video_id(url)
        if not video_id:
            await message.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ.")
            return
        video_title = get_video_title(video_id)
        query = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        caption = (
            f"<b>[{video_title}](https://t.me/{app.username}?start=info_{video_id})</b>"
        )
        await message.reply_photo(query, caption=caption)
        await a.delete()
    except requests.exceptions.RequestException:
        await a.edit("ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ғᴇᴛᴄʜɪɴɢ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ.")
    except Exception as e:
        await a.edit("ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")
        print(f"ᴇʀʀᴏʀ: {e}")
