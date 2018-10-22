import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import asyncio
import time
import os







class SmashFest:
    owner = "MSU | BlueFlare10"
    participants = {}
    location = "Communication Arts Building, Room 154"
    startTime = "6:00 PM"
    initialMonitors = 0
    initialSetups = 0
    monitors = 0
    numSetups = 0

    def __init__(self, owner, location, startTime):
        self.owner = owner
        self.location = location
        self.startTime = startTime

    def __del__(self):
        self.participants.clear()
        self. initialMonitors = 0
        self.initialSetups = 0
        self.monitors = 0
        self.numSetups = 0

    def addParticipants(self, participant, setup, monitor):
        self.addParticipant(participant, setup, monitor)

    def tostr(self, index):
        output = "Smashfest #%s Owner: %s Location: %s Time: %s Setups: %s Monitors: %s\n" % (index + 1, self.owner, self.location, self.startTime, self.getSetups(), self.getMonitors())
        return output

    def addParticipant(self, person, setup, monitor):
        setup = setup.strip()
        monitor = monitor.strip()
        if setup == "yes" or int(setup) > 0:
            setup = 1
        else:
            setup = 0
        if monitor == "yes" or int(monitor) > 0:
            monitor = 1
        else:
            monitor = 0
        info = (setup, monitor)
        self.participants[person] = info

    def listParticipants(self):
        output = ""
        for participant in self.participants:
            output = output + participant + ", "
        output = output[:-2]
        if output == "":
            output = "No participants :("
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
            info = self.participants[participant]
            if info[0] == 1 or info[0] == '1':
                setups += 1
            if info[1] == 1 or info[1] == '1':
                monitors += 1
            self.monitors = monitors
            self.numSetups = setups





smashfests = list()
Client = discord.Client()
client = commands.Bot(command_prefix = ".")

bdubs_emoji = "Yay BDubs"



@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Smash Ultimate"))

@client.event
async def on_message(message):
    originalMessage = message.content
    message.content = message.content.lower()
    if message.author.id == client.user.id:
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
        msg = bdubs_emoji
        await client.send_message(message.channel, msg)
    if message.content.startswith("!carter"):
        msg = "Money match me {0.author.mention}, you won't".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith("!taylor"):
        rand = random.randint(0, 4)
        msg = ""
        if rand == 0:
            msg = "I love Robin"
        elif rand == 1:
            msg = "I love Chrom"
        elif rand == 2:
            msg = "I love Rein"
        elif rand == 3:
            msg = "I love McCree"
        elif rand == 4:
            msg = "I love All Might"

        await client.send_message(message.channel, msg)
    if message.content.startswith("!cherpumple"):
        rand = random.randint(0, 5)
        msg = "Did you mean "
        if rand == 0:
            msg = msg + "Cherpumpled?"
        elif rand == 1:
            msg = msg + "Cherpipele?"
        elif rand == 2:
            msg = msg + "Cherpumsle?"
        elif rand == 3:
            msg = msg + "Chairpumple?"
        elif rand == 4:
            msg = msg + "Cherfluffle?"
        elif rand == 5:
            msg = msg + "Cherple?"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!goma"):
        msg = "Another Dr. Pepper please"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!dyl"):
        msg = "DILL PICKLE"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!j3"):
        msg = "Did you mean sick Mario?"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!help"):
        await client.send_message(message.channel, "!create/LOCATION/START TIME/NUMBER OF SETUPS IN ROOM/NUMBER OF MONITORS IN ROOM    Creates a smashfest that others can join")
        await client.send_message(message.channel, "!list/SMASHFEST NUMBER                                                             Lets you view information about a smashfest")
        await client.send_message(message.channel, "!addme/SMASHFEST NUMBER/BRINGING A SETUP/BRINGING A MONITOR                        Lets you join a smashfest")
        await client.send_message(message.channel, "!removeme/SMASHFEST NUMBER                                                         Removes you from a smashfest")
        await client.send_message(message.channel, "!participants/SMASHFEST NUMBER                                                     Displays the participants of a smashfest")
        await client.send_message(message.channel, "!setups/SMASHFEST NUMBER                                                           Displays how many setups are at a fest")
        await client.send_message(message.channel, "!monitors/SMASHFEST NUMBER                                                         Displays how many monitors are at a fest")
        await client.send_message(message.channel, "!end/SMASHFEST NUMBER                                                              Ends a smashfest")



    if message.content.startswith("!create"):
        try:
            messageString = str(originalMessage)
            parts = messageString.split("/")
            sf = SmashFest(str(message.author), parts[1], parts[2])
            sf.initialSetups = int(parts[3])
            sf.initialMonitors = int(parts[4])
            smashfests.append(sf)
            msg = "Created smashfest, currently %s smashfest(s) planned" % len(smashfests)
        except IndexError:
            msg = "Format your message like this(don't include parentheses): !create/Snyphi Basement(Location)/7:34 PM(Start Time)/1(Setup)/2(monitors)"
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
                fest = int(parts[1]) - 1
                if fest < 0:
                    await client.send_message(message.channel, "Please enter a positive numbered smashfest")
                    return
                setup = parts[2]
                monitor = parts[3]
                smashfests[fest].addParticipant(str(message.author), setup, monitor)
                msg = "Added you to smashfest #%s {0.author.mention}".format(message) % (fest + 1)
                for smashfest in smashfests:
                    print(smashfest.participants)
            except IndexError or TypeError:
                msg = "Format your message like this: !addme/1(Smashfest number)/yes(Setup)/no(Monitor) If you used correct formatting check the smashfest number with !list"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)

    if message.content.startswith("!removeme"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                fest = int(parts[1])
                if fest < 0:
                    await client.send_message(message.channel, "Please enter a positive numbered smashfest")
                    return
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
                fest = int(parts[1]) - 1
                if fest < 0:
                    await client.send_message(message.channel, "Please enter a positive numbered smashfest")
                    return
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
                fest = int(parts[1]) - 1
                if fest < 0:
                    await client.send_message(message.channel, "Please enter a positive numbered smashfest")
                    return
                setups = smashfests[fest].getSetups()
                participants = len(smashfests[fest].participants)
                monitors = smashfests[fest].getMonitors()
                msg = "Smashfest #%s has %s participant(s), %s monitor(s) and %s setup(s)" % (fest + 1, participants, monitors, setups)
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
                index = int(parts[1]) - 1
                if index < 0:
                    await client.send_message(message.channel, "Please enter a positive numbered smashfest")
                    return

                sender = str(message.author)
                owner = smashfests[index].owner

                if sender != owner:
                    msg = "You're not the owner of this fest!"
                else:
                    smashfests.pop(index)
                    msg = "Removed smashfest #%s" % (index + 1)
            except IndexError or TypeError:
                msg = "Format your message like this: !end/1"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)


client.run('NTAyNTg5MzM2NzA2MDg4OTYy.Dqqr3w.vQdTF0dW6yiT8e8X_e8ZqcCEF1w')