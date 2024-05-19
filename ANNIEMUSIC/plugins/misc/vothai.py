import random

from pyrogram import Client, filters
from ANNIEMUSIC import app

# List of your GIF URLs
KICK_GIF_URLS = [
    "https://telegra.ph/file/d147ade81c7d9f9aaf7f7.mp4",
    "https://telegra.ph/file/d310b1615f80c4238bd48.mp4",
    "https://telegra.ph/file/0347fe9124af750c4e470.mp4",
    # Add more URLs as needed
]

@app.on_message(filters.command("kick") & ~filters.forwarded & ~filters.via_bot)
def slap_command(client, message):
    try:
        sender = message.from_user.mention(style='markdown')

        target = sender if not message.reply_to_message else message.reply_to_message.from_user.mention(style='markdown')

        msg = f"{sender} Vuttan parru oru vothai {target}! 😒"

        # Select a random GIF URL from the list
        random_gif_url = random.choice(KICK_GIF_URLS)

        message.reply_animation(animation=random_gif_url, caption=msg)
        
    except Exception as e:
        message.reply_text(f"An unexpected error occurred: {str(e)}")
