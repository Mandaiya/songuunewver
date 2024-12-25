from pyrogram import Client, filters
from ANNIEMUSIC import app
import time

# Dictionary to store scores, overs, and round results
scores = {}
overs = {}
round_scores = {}
last_command_time = {}
levels = {}

# Constants
OVERS_LIMIT = 6
WINNING_SCORE = 1000
LEVEL_THRESHOLD = 50
FLOOD_WAIT_TIME = 180  # 3 minutes in seconds

@app.on_message(filters.command("bat"))
async def bat(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    current_time = time.time()

    # Flood wait control
    if user_id in last_command_time and current_time - last_command_time[user_id] < FLOOD_WAIT_TIME:
        remaining_time = int(FLOOD_WAIT_TIME - (current_time - last_command_time[user_id]))
        await message.reply_text(f"⚠️ Please wait {remaining_time} seconds before using /bat again.", quote=True)
        return
    
    last_command_time[user_id] = current_time

    # Initialize player stats
    if user_id not in scores:
        scores[user_id] = 0
    if user_id not in overs:
        overs[user_id] = 0
    if user_id not in round_scores:
        round_scores[user_id] = 0
    if user_id not in levels:
        levels[user_id] = 0

    x = await bot.send_dice(chat_id, "🎲")
    m = x.dice.value
    current_score = scores[user_id]
    current_over = overs[user_id]

    if m == 3:
        await message.reply_text(f"Oops! You're out! Your score for this over is: {current_score}", quote=True)
        scores[user_id] = 0
        overs[user_id] = 0
        round_scores[user_id] = 0
    elif m == 5:
        scores[user_id] += 1
        await message.reply_text(f"Extra run! Your score for this over is: {scores[user_id]}", quote=True)
    elif m in [1, 2, 4, 6]:
        scores[user_id] += m
        await message.reply_text(f"You scored {m} runs! Your current score is: {scores[user_id]}", quote=True)

    overs[user_id] += 1
    round_scores[user_id] = scores[user_id]

    if overs[user_id] == OVERS_LIMIT:
        await message.reply_text(f"End of the over! Your total score for the over is: {scores[user_id]}", quote=True)
        overs[user_id] = 0

        round_winner = None
        highest_score = -1
        for player_id, score in round_scores.items():
            if score > highest_score and score != 0:
                highest_score = score
                round_winner = player_id

        if round_winner:
            levels[round_winner] += 1
            await bot.send_message(round_winner, f"🎉 You won this round! Your level is now: {levels[round_winner]}")

        round_scores.clear()

    for user_id, level in levels.items():
        if level >= LEVEL_THRESHOLD:
            scores[user_id] += 5  # Reward points only if level >= 50
            await message.reply_text(f"🌟 {message.from_user.mention} has reached level {level} and earned 5 points!", quote=True)
            levels[user_id] = 0

@app.on_message(filters.command("cricketscore"))
async def leaderboard(bot, message):
    leaderboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    leaderboard_text = "\ud83c\udfc6 **Leaderboard** \ud83c\udfc6\n\n"

    for idx, (user_id, score) in enumerate(leaderboard[:10], 1):
        user = await bot.get_users(user_id)
        leaderboard_text += f"{idx}. {user.first_name} - {score} runs\n"

    if not leaderboard:
        leaderboard_text = "No players yet."

    await message.reply_text(leaderboard_text, quote=True)

__help__ = """
Play Cricket Game:
- /bat - Bat 🎲 Roll the dice and score runs!
- /cricketscore - Show the leaderboard

Game Rules:
- Dice roll '3' = out
- Dice roll '5' = extra run
- Rolls of '1', '2', '4', '6' = runs
- 6 balls = 1 over
- Winning a round = +1 level
- Reach level 50 = 5 points
- Flood wait = 3 mins between /bat commands
"""

__mod_name__ = "Cricket game"
