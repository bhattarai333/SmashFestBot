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
        if not type(setup) == int:
            setup = setup.strip()
        if not type(monitor) == int:
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