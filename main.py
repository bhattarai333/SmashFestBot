import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os







class SmashFest:
    owner = "MSU | BlueFlare10"
    participants ={}
    location = "Communication Arts Building, Room 154"
    startTime = "6:00 PM"
    initialMonitors = 0
    initialSetups = 0
    monitors = 0
    numSetups = 0

    def __init__(self, owner, location, startTime):
        self.owner = owner#str.split(owner, '#')[0]
        self.location = location
        self.startTime = startTime

    def addParticipants(self, participant, setup, monitor):
        self.addParticipant(participant, setup, monitor)

    def tostr(self, index):
        output = "Smashfest #%s Owner: %s Location: %s Time: %s Setups: %s Monitors: %s\n" % (index, self.owner, self.location, self.startTime, self.getSetups(), self.getMonitors())
        return output

    def addParticipant(self, person, setup, monitor):
        setup = setup.trim()
        monitor = monitor.trim()
        if setup == "yes":
            setup = 1
        else:
            setup = 0
        if monitor == "yes":
            monitor = 1
        else:
            setup = 0
        info = (setup, monitor)
        self.participants[person] = info

    def listParticipants(self):
        output = ""
        for participant in self.participants:
            output = output + participant + ", "
        output = output[:-2]
        return output

    def addSetup(self):
        self.numSetups += 1

    def getSetups(self):
        self.findInfo()
        return self.numSetups + self.initialSetups

    def addMonitor(self):
        self.monitors += 1

    def getMonitors(self):
        self.findInfo()
        return self.monitors + self.initialMonitors

    def findInfo(self):
        setups = 0
        monitors = 0
        for participant in self.participants:
            if participant[0] == 1:
                setups += 1
            if participant[1] == 1:
                monitors += 1
            self.monitors = monitors
            self.numSetups = setups





Client = discord.Client()
client = commands.Bot(command_prefix = ".")


smashfests = list()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Smash Ultimate"))

@client.event
async def on_message(message):
    originalMessage = message.content
    message.content = message.content.lower()
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
        msg = ":bdubs:"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!carter"):
        msg = "Money match me {0.author.mention}, you won't".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!create"):
        try:
            messageString = str(originalMessage)
            parts = messageString.split("/")
            sf = SmashFest(str(message.author), parts[1], parts[2])
            sf.initialSetups = (parts[3])
            sf.initialMonitors = (parts[4])
            smashfests.append(sf)
            msg = "Created smashfest, currently %s smashfest(s) planned" % len(smashfests)
        except IndexError:
            msg = "Format your message like this(don't include parentheses): !create/Snyphi Basement(location)/7:34 PM(Start Time)/1(setup)/2(monitors)"
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
                setup = parts[2]
                monitor = parts[3]
                smashfests[fest].addParticipant(str(message.author), setup, monitor)
                msg = "Added you to smashfest #%s {0.author.mention}".format(message) % fest
            except IndexError or TypeError:
                msg = "Format your message like this: !addme/1(Smashfest number)/yes(setup)/no(monitor)"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!removeme"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                fest = int(parts[1])
                smashfests[fest].addParticipant(str(message.author))
                msg = "Removed you from smashfest #%s {0.author.mention}".format(message) % fest
            except IndexError or TypeError:
                msg = "Format your message like this: !removeme/1(Smashfest number)"
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
                msg = "Format your message like this: !participants/1(Smashfest number)"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!setups") or message.content.startswith("!monitors"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                fest = int(parts[1])
                setups = smashfests[fest].getSetups()
                participants = len(smashfests[fest].participants)
                monitors = smashfests[fest].getMonitors()
                msg = "Smashfest #%s has %s participant(s), %s monitor(s) and %s setup(s)" % (fest, participants, monitors, setups)
            except IndexError or TypeError:
                msg = "Format your message like this: !setups/1(Smashfest number)"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)


    if message.content.startswith("!end"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                index = int(parts[1])

                sender = str(message.author)
                owner = smashfests[index].owner

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