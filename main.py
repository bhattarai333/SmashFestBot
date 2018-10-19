import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("hello")
    await client.change_presence(game=discord.Game(name="videos"))

@client.event
async def on_message(message):
    if message.content.startswith('.hello'):
        msg = 'Hello {0.author.mention} How are you today?'.format(message)
        await client.send_message(message.channel,msg)

client.run('NTAyNTg5MzM2NzA2MDg4OTYy.Dqqr3w.vQdTF0dW6yiT8e8X_e8ZqcCEF1w')
print('running')