from pyrogram import Client, filters
import random
from ANNIEMUSIC import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "Love is in the air but needs a little spark.",
            "A good start but there's room to grow.",
            "It's just the beginning of something beautiful."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "A strong connection is there. Keep nurturing it.",
            "You've got a good chance. Work on it.",
            "Love is blossoming, keep going."
        ])
    else:
        return random.choice([
            "I fall in love with you all over again every time I see you",
            "I can’t imagine going through this life without you by my side.",
            "I’ll love you forever and always."
        ])

def get_random_gif():
    gifs = [
        "https://telegra.ph/file/6163534b1adda7e693829.mp4",  # Random GIF 1
        "https://telegra.ph/file/6bc43743efc0c9372750f.mp4",  # Random GIF 2
        "https://telegra.ph/file/0c6f05f5c65065b6bd273.mp4",  # Random GIF 3
        "https://telegra.ph/file/a94863a86d2e9f0fa42db.mp4",  # Random GIF 4
    ]
    return random.choice(gifs)

@app.on_message(filters.command("love", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1} 💕 + {name2} 💕 = {love_percentage}%\n\n{love_message}"
        
        # Check if it's an exact match (love percentage is 100%)
        if love_percentage == 100:
            gif_url = get_random_gif()
            app.send_animation(message.chat.id, gif_url)
    else:
        response = "Please enter two names after /love command."
    app.send_message(message.chat.id, response)
