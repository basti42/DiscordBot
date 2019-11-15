import os
import random
import atexit

from helpers.CoinbaseGetter import CoinbaseGetter
from helpers.CommandLogger import CommandLogger
from datetime import datetime

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
guild = os.getenv("DISCORD_GUILD")

# setup the bot class
bot = commands.Bot(command_prefix="!")
cmdlogger = CommandLogger()

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord Server '{guild}'")


# implement all bot commands
@bot.command("hello", help="Just say hello to each other")
async def hello(ctx):
    cmdlogger.logContext(ctx)
    caller = ctx.author.name
    await ctx.send("Hello, {}!".format(caller))


@bot.command("btc", help="get the current BTC price in €")
async def btc(ctx):
    cmdlogger.logContext(ctx)
    cbg = CoinbaseGetter()
    now = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    value = cbg.getPriceFor("bitcoin")
    await ctx.send("1 BTC = {} @ {}".format(value, now))


@bot.command("eth", help="get the current ETHEREUM price in €")
async def btc(ctx):
    cmdlogger.logContext(ctx)
    cbg = CoinbaseGetter()
    now = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    value = cbg.getPriceFor("ethereum")
    await ctx.send("1 ETH = {} @ {}".format(value, now))


@bot.command("iota", help="get the current IOTA price in €")
async def btc(ctx):
    cmdlogger.logContext(ctx)
    cbg = CoinbaseGetter()
    now = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    value = cbg.getPriceFor("iota")
    await ctx.send("1 MIOTA = {} @ {}".format(value, now))



# make sure the database gets closed before exiting
def exit_handler():
    print("\r[*] Closing Database connections ... ", end="")
    cmdlogger.closeLogger()
    print("\r[!] Closing Database connections ... DONE")

atexit.register(exit_handler)



bot.run(token)
