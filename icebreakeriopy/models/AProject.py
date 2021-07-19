from .AMachine import AMachine


class AProject:
    def __init__(self, path, aVersion=None, directoryOfConfigs=None, machines=None):
        self.path = path
        self.aVersion = aVersion
        self.directoryOfConfigs = directoryOfConfigs

        if type(machines) != list:
            self.machines = []
        else:
            self.machines = machines

    def parseMachinesFromJsonList(self, machines=None):
        if type(machines) == list:
            for machineJSON in machines:
                aMachine = AMachine(name=machineJSON.get("name"),
                                    parentAProject=self)
                aMachine.parseReposFromJsonList(machineJSON.get("repos"))
                aMachine.parseConfigsFromJsonList(machineJSON.get("configs"))
                self.machines.append(aMachine)
