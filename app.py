import discord
from discord.ext import commands
import json
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

phrases = []
with open('cookie.txt', 'r') as asset_txt:
    for line in asset_txt:
        phrases.append(line.strip())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def cookie(message):
    await message.channel.send(random.choice(phrases))

bot.run(os.getenv("TOKEN"))