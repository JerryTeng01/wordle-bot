import discord
from discord.ext import commands
from datetime import date
from yaml import safe_load

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

with open("secrets.yaml") as f:
        config = safe_load(f)

@bot.event
async def on_ready():
    today = date.today()
    formatted_date = today.strftime("%m/%d/%Y")
    try:
        guild_id = config["SERVER"]
        guild = bot.get_guild(guild_id)

        channel_id = config["CHANNEL"]
        channel = guild.get_channel(channel_id)

        message = await channel.send("🖕 New Wordle just dropped 🖕")

        thread = await message.create_thread(name=f"{formatted_date} Wordle thread", reason="Why not")
        print(f'Thread: {thread.mention}')

    except Exception as e:
        print(f'Error: {e}')

    # Close the bot after creating the thread
    await bot.close()

# Run the bot with your token
bot.run(config["TOKEN"])
