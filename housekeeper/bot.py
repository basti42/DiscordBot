import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
guild = os.getenv("DISCORD_GUILD")

# setup the bot class
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord Server '{guild}'")


# implement all bot commands
@bot.command("hello", help="Just say hello to each other")
async def hello(ctx):
    caller = ctx.author.name
    await ctx.send("Hello, {}!".format(caller))


bot.run(token)
