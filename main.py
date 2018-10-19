import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os







class SmashFest:
    owner = "MSU | BlueFlare10"
    participants = list()
    location = "Communication Arts Building, Room 154"
    startTime = "6:00 PM"
    currentSetups = 0
    numSetups = 0

    def __init__(self, owner, location, startTime):
        self.owner = str.split(owner, '#')[0]
        self.location = location
        self.startTime = startTime

    def addParticipants(self, participant):
        self.participants.append(participant)







Client = discord.Client()
client = commands.Bot(command_prefix = ".")


smashfests = list()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Smash Ultimate"))

@client.event
async def on_message(message):
    message.content = message.content.lower()
    message.server
    if message.author == "Smashfest Bot#9788":
        return


    if message.content.startswith('!hello') or message.content.startswith("!hi"):
        msg = 'Hello {0.author.mention} How are you today?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!mario"):
        msg = "J3's Mario is sick af"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!69"):
        msg = "Nice"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!ness"):
        msg = "Ness sux"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!mario"):
        msg = "J3 has a sick Mario"
        await client.send_message(message.channel, msg)

    if message.content.startswith("pizza house"):
        msg = "BDubs is better"
        await client.send_message(message.channel, msg)

    if message.content.startswith("bdubs"):
        msg = ":bdubs: %s" % message.author
        await client.send_message(message.channel, msg)

    if message.content.startswith("!carter"):
        msg = "Money match me {0.author.mention}, you won't".format(message)
        await client.send_message(message.channel, msg)



Bot = commands.Bot(command_prefix="!create")
@client.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

client.run('NTAyNTg5MzM2NzA2MDg4OTYy.Dqqr3w.vQdTF0dW6yiT8e8X_e8ZqcCEF1w')