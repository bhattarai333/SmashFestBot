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

    def tostr(self, index):
        output = "Smashfest #%s Owner: %s Location: %s Time: %s Setups: %s\n" % (index, self.owner, self.location, self.startTime, self.numSetups)
        return output

    def addParticipant(self, person):
        self.participants.append(person)

    def listParticipants(self):
        output = ""
        for participant in self.participants:
            output = output + participant + ", "
        output = output[:-2]
        return output

    def addSetup(self):
        self.numSetups += 1

    def getSetups(self):
        return self.numSetups





Client = discord.Client()
client = commands.Bot(command_prefix = ".")


smashfests = list()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Smash Ultimate"))

@client.event
async def on_message(message):
    sender = message.author
    if sender == "Smashfest Bot#9788":
        return
    originalMessage = message.content
    message.content = message.content.lower()

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
        msg = ":bdubs:"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!carter"):
        msg = "Money match me {0.author.mention}, you won't".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!create"):
        try:
            messageString = str(originalMessage)
            print("MESSAGE: %s" % messageString)
            parts = messageString.split("/")
            print(parts)
            sf = SmashFest(sender, parts[1], parts[2])
            smashfests.append(sf)
            msg = "Created smashfest, currently #%s smashfest(s) planned" % len(smashfests)
        except IndexError:
            msg = "Format your message like this: !create/Snyphi Basement/7:34 PM"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!list"):
        msg = ""
        if not len(smashfests) == 0:
            for index, smashfest in enumerate(smashfests):
                msg = msg + smashfest.tostr(index)
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!addme"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                fest = int(parts[1])
                smashfests[fest].addParticipant(str(message.author))
                msg = "Added you to smashfest #%s {0.author.mention}".format(fest, message) % fest
            except IndexError or TypeError:
                msg = "Format your message like this: !addme/1"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!participants"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                fest = int(parts[1])
                msg = smashfests[fest].listParticipants()
            except IndexError or TypeError:
                msg = "Format your message like this: !participants/1"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!setups"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                fest = int(parts[1])
                setups = smashfests[fest].getSetups()
                participants = len(smashfests[fest].participants)
                msg = "Smashfest #%s has %s participant(s) and %s setup(s)" % (fest, participants, setups)
            except IndexError or TypeError:
                msg = "Format your message like this: !setups/1"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!end"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                index = int(parts[1])


                owner = smashfests[index].owner

                print("S: %s O:%s" % (sender, owner))

                if sender != owner:
                    msg = "You're not the owner of this fest!"
                else:
                    smashfests.pop(index)
                    msg = "Removed smashfest #%s" % index
            except IndexError or TypeError:
                msg = "Format your message like this: !end/1"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)




client.run('NTAyNTg5MzM2NzA2MDg4OTYy.Dqqr3w.vQdTF0dW6yiT8e8X_e8ZqcCEF1w')