import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import asyncio
import time
import os
import json
import requests





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
        self.participants = {}
        self.location = location
        self.startTime = startTime
        self.initialSetups = 0
        self.initialMonitors = 0
        self.monitors = 0
        self.numSetups = 0

    def __del__(self):
        self.participants.clear()
        self. initialMonitors = 0
        self.initialSetups = 0
        self.monitors = 0
        self.numSetups = 0

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

    def removeParticipant(self, person):
        self.participants.pop(person, None)

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
weekly_prereg_link = "No weekly prereg link set ;("
commentary_prereg_link = "No commentary prereg link set ;("
Client = discord.Client()
client = commands.Bot(command_prefix = "!")

bdubs_emoji = "Yay BDubs"
version = "**SmashFest Bot v2.1.3**"
pickle_counter = 0


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Smash Ultimate"))
    f = open("data.json", 'r')
    print(f)


@client.event
async def on_message(message):
    originalMessage = message.content
    message.content = message.content.lower()
    if message.author.id == client.user.id:
        return
    time.sleep(0.2)
    if message.content.startswith('!hello') or message.content.startswith("!hi"):
        msg = 'Hello {0.author.mention} How are you today?'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith("!sick"):
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
        rand = random.randint(0, 6)
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
        elif rand == 6:
            msg = msg + "Chermpurple?"
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
    if message.content.startswith("!mm") or message.content.startswith("!moneymatch"):
        msg = "me Carter";
        await client.send_message(message.channel, msg)
    if message.content.startswith("!slam") or message.content.startswith("!danny"):
        msg = "Don't get greedy!"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!nebula"):
        msg = "Go to sleep"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!shiva"):
        msg = "THE LEGEND!"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!cri"):
        msg = "yank"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!sam"):
        msg = "Please... Please prereg"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!flare") or message.content.startswith("!blueflare10"):
        rand = random.randint(0, 8)
        msg = "_"
        if rand == 0:
            msg = "Did you see my sick Fortnite win?"
        elif rand == 1:
            msg = "I had to do it to em haha amirite guise?"
        elif rand == 2:
            msg = "Something something dragons something"
        elif rand == 3:
            msg = "I'm secretly in love with Bowser and his thicc necc"
        elif rand == 4:
            msg = "Yikes"
        elif rand == 5:
            msg = "STOP YOUR FRIENDLIES... Guys seriously, stop your friendlies.. guys please"
        elif rand == 6:
            msg = "Guys my bayo kinda clean"
        elif rand == 7:
            msg = "Technically, in the last month, only counting in the SnyPhi Basement, only after 8:00 PM, I've only lost 3 money matches so far"
        elif rand == 8:
            msg = "Ridley"

        await client.send_message(message.channel, msg)
    if message.content.startswith("!nog"):
        msg = "https://raw.githubusercontent.com/bhattarai333/bhattarai333.github.io/master/docs/Resources/memes/nog.jpg"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!nofun"):
        msg = "https://raw.githubusercontent.com/bhattarai333/bhattarai333.github.io/master/docs/Resources/memes/president.png"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!j\'haira") or message.content.startswith("!jhaira"):
        msg = "Did someone say PM?"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!justin"):
        rand = random.randint(0, 2)
        msg = "_"
        if rand == 0:
            msg = "Chicken Tendies"
        elif rand == 1:
            msg = "Chocy Milk"
        elif rand == 2:
            msg = "Sheik is a midtier character"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!matador"):
        msg = "Little Mac actually wins that MU"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!aaron") or message.content.startswith("!ogre"):
        rand = random.randint(0, 3)
        msg = "_"
        if rand == 0:
            msg = "Shadow Ball!"
        elif rand == 1:
            msg = "Something something bdubs sux something im dum"
        elif rand == 2:
            msg = "Get outta my swamp"
        elif rand == 3:
            msg = "\*likes your tweet\*"
        elif rand == 4:
            msg = "Who's tryna play rivals?"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!mikau") or message.content.startswith("!evan"):
        msg = "NO ANIME ALLOWED"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!bread"):
        msg = "Let's get this BDubs!"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!dayman"):
        msg = "Money match me in Pokemon Snap"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!mo"):
        msg = "Did you mean Nebula echo fighter?"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!mika") and not message.content.startswith("!mikau"):
        rand = random.randint(0, 1)
        msg = "_"
        if rand == 0:
            msg = "I wanted to say something annoying and philosophical about staples but I can’t think of something"
        elif rand == 1:
            msg = "***vibrates angrily***"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!pickle"):
        global pickle_counter
        pickle_counter = pickle_counter + 1
        msg = "I'm kinda nice #%s" % pickle_counter
        await client.send_message(message.channel, msg)
    if message.content.startswith("!caps"):
        msg = "Mii Swordfighter sux, sry bruh"
        await client.send_message(message.channel, msg)


    if message.content.startswith("!version"):
        msg = version
        await client.send_message(message.channel, msg)
    if message.content.startswith("!thank"):
        msg = "You are very welcome, I live to serve"
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
    if message.content.startswith("!about"):
        msg = "Hello, I am %s, created to help MSU students find places to play Smash 4/Smash Ultimate on campus. Direct any inquiries to J3(Josh Bhattarai).\n" % version
        msg = msg + "Written in Python 3.7, running in a free hosted Heroku Python 3.6.6 enviornment. Uses Discord.py by Rapptz.\n"
        msg = msg + "Please follow the MSU Smash 4 Twitter: https://twitter.com/msusmash4"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!esa"):
        msg = "I'm sorry for posting inappropriate images :("
        await client.send_message(message.channel, msg)
    if message.content.startswith("!setpriyank"):
        messageString = str(originalMessage)
        parts = messageString.split("/")
        full_string = ""
        for index, part in enumerate(parts):
            if index == 0:
                continue
            full_string = full_string + part + '/'
        full_string = full_string[0:-1]
        global weekly_prereg_link
        weekly_prereg_link = full_string
        save_data()


    if message.content.startswith("!facebook"):
        msg = "https://www.facebook.com/groups/MSUSmash4/"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!twitter"):
        msg = "https://twitter.com/MSUsmash4"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!youtube"):
        msg = "https://www.youtube.com/channel/UCvMLi4Iq6xYDRnjc6eJ4IhA"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!challonge"):
        msg = "https://spartanweeklies.challonge.com/"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!discord"):
        msg = "ESA Discord: https://discord.gg/56v3F6a\nMSU Smash4 Discord: https://discord.gg/Y9QRDqh"
        await client.send_message(message.channel, msg)
    if message.content.startswith("!prereg"):
        msg = weekly_prereg_link
        await client.send_message(message.channel, msg)


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
        save_data()

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
            except IndexError or TypeError:
                msg = "Format your message like this: !addme/1(Smashfest number)/yes(Setup)/no(Monitor) If you used correct formatting check the smashfest number with !list"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)
        save_data()

    if message.content.startswith("!removeme"):
        if not len(smashfests) == 0:
            try:
                messageString = str(originalMessage)
                parts = messageString.split("/")
                fest = int(parts[1]) - 1
                if fest < 0:
                    await client.send_message(message.channel, "Please enter a positive numbered smashfest")
                    return
                smashfests[fest].removeParticipant(str(message.author))
                msg = "Removed you from smashfest #%s {0.author.mention}".format(message) % (fest + 1)
            except IndexError or TypeError:
                msg = "Format your message like this: !removeme/1(Smashfest number)"
        else:
            msg = "There are no current smashfests, try creating one with !create"
        await client.send_message(message.channel, msg)
        save_data()

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


    if message.content.startswith("!end") or message.content.startswith("!delete"):
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
        save_data()

def save_data():
    global smashfests
    global weekly_prereg_link
    global commentary_prereg_link

    data = {}
    data["smashfests"] = json.dumps([ob.__dict__ for ob in smashfests])
    data["weekly_prereg_link"] = weekly_prereg_link
    data["commentary_prereg_link"] = commentary_prereg_link

    headers = {'content-type': 'application/json'}
    response = requests.post("https://api.jsonbin.io/b", json.dump(data), headers=headers)
    print(response.text)

client.run(os.environ.get("TOKEN"))