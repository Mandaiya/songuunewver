import random

from pyrogram import Client, filters
from ANNIEMUSIC import app

# List of your GIF URLs
MOGARA_GIF_URLS = [
    "https://telegra.ph/file/ad6aaa917c47cffafeffc.mp4"
    # Add more URLs as needed
]

@app.on_message(filters.command("mogara") & ~filters.forwarded & ~filters.via_bot)
def mogara_command(client, message):
    try:
        sender = message.from_user.mention(style='markdown')

        target = sender if not message.reply_to_message else message.reply_to_message.from_user.mention(style='markdown')

        msg = f"{sender} Jumbalikaa pilapi {target}! 🤣"

        # Select a random GIF URL from the list
        random_gif_url = random.choice(MOGARA_GIF_URLS)

        message.reply_animation(animation=random_gif_url, caption=msg)
        
    except Exception as e:
        message.reply_text(f"An unexpected error occurred: {str(e)}")
