from pyrogram import Client, filters
from ANNIEMUSIC import app

# Dictionary to store scores for each player
scores = {}

@app.on_message(filters.command("bat"))
async def bat(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # Initialize score for the user if not already exists
    if user_id not in scores:
        scores[user_id] = 0

    # Send a cricket emoji to start the over
    x = await bot.send_dice(chat_id, "🏏")  # Use cricket emoji
    m = x.dice.value
    
    # Update score
    scores[user_id] += m
    
    # Check if the over is completed (every 6th ball)
    if scores[user_id] % 6 == 0:
        await message.reply_text(f"End of the over! Your total score is: {scores[user_id]}", quote=True)
        scores[user_id] = 0
    else:
        await message.reply_text(f"Your current score is: {scores[user_id]}", quote=True)

__help__ = """
Play Cricket Game:
/bat - Bat 🏏
"""

__mod_name__ = "Cʀɪᴄᴋᴇᴛ Gᴀᴍᴇ"
