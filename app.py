import discord
from discord import app_commands
from discord.ext import commands
import json
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

phrases = []
with open('cookie.txt', 'r') as asset_txt:
    for line in asset_txt:
        phrases.append(line.strip())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(f'Error: {e}')

@bot.tree.command(name='cookie')
async def cookie(interaction: discord.Intents):
    await interaction.response.send_message(random.choice(phrases))

bot.run(os.getenv("TOKEN"))