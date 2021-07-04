from .AMachine import AMachine


class AProject:
    def __init__(self, aVersion=None, pathToCfg=None, machines=None):
        self.__aVersion = aVersion
        self.__pathToCfg = pathToCfg

        if type(machines) != list:
            self.__machines = []
        else:
            self.__machines = machines

    def parseMachinesFromJsonList(self, machines=None):
        if type(machines) == list:
            for machineJSON in machines:
                aMachine = AMachine(name=machineJSON.get("name"))
                aMachine.parseReposFromJsonList(machineJSON.get("repos"))
                self.__machines.append(aMachine)

    def get_aVersion(self):
        return self.__aVersion

    def get_machines(self):
        return self.__machines
