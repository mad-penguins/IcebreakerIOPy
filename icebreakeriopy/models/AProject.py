from .AMachine import AMachine


class AProject:
    def __init__(self, aVersion=None, pathToCfg=None, machines=None):
        self.aVersion = aVersion
        self.pathToCfg = pathToCfg

        if type(machines) != list:
            self.machines = []
        else:
            self.machines = machines

    def parseMachinesFromJsonList(self, machines=None):
        if type(machines) == list:
            for machineJSON in machines:
                aMachine = AMachine(name=machineJSON.get("name"))
                aMachine.parseReposFromJsonList(machineJSON.get("repos"))
                self.machines.append(aMachine)
