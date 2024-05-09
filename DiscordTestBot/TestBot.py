import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am a Bot!")


#token
bot.run('token')
