import os
import random

from helpers.CoinbaseGetter import CoinbaseGetter
from datetime import datetime

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


@bot.command("btc", help="get the current BTC price in €")
async def btc(ctx):
    cbg = CoinbaseGetter()
    now = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    value = cbg.getPriceFor("bitcoin")

    # user = ctx.author
    # name = user.name
    # id = user.id
    # content = ctx.message.content
    # channel = ctx.message.channel.name
    # print("{}[{}] sent {} in {}".format(name, id, content, channel))
    await ctx.send("1 BTC = {} @ {}".format(value, now))


@bot.command("eth", help="get the current ETHEREUM price in €")
async def btc(ctx):
    cbg = CoinbaseGetter()
    now = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    value = cbg.getPriceFor("ethereum")
    await ctx.send("1 ETH = {} @ {}".format(value, now))

@bot.command("iota", help="get the current IOTA price in €")
async def btc(ctx):
    cbg = CoinbaseGetter()
    now = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    value = cbg.getPriceFor("iota")
    await ctx.send("1 MIOTA = {} @ {}".format(value, now))



bot.run(token)
