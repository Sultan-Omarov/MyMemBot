import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Привет! Меня зовут {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def leg(ctx):
    legen = os.listdir('legen')
    img_name = random.choice(legen)
    with open(f'legen/{img_name}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def people(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def old(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def young(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    animal = os.listdir('animal')
    an_name = random.choice(animal)
    with open(f'animal/{an_name}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

bot.run("")
