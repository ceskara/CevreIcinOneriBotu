import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command() # command = komut
async def Yetiskin(ctx):
    """Adds two numbers together."""
    with open('yetiskinlere.txt', 'r', encoding='utf8') as f:
        yetiskinler = f.readlines()
    with open('topluTasimaFoto.webp', 'rb') as f:
        resim = discord.File(f)
    await ctx.send(random.choice(yetiskinler)), await ctx.send(file=resim)


@bot.command()
async def Gencler(ctx):
    """Adds two numbers together."""
    random_number = random.randint(0, 1)
    with open('gencler.txt', 'r', encoding='utf8') as f:
        gencler = f.readlines()
    with open(f'Gencler{random_number}.jpg', 'rb') as f:
        resim = discord.File(f)
    await ctx.send(gencler[random_number]), await ctx.send(file=resim)



bot.run('Token Buraya Gelecek')
