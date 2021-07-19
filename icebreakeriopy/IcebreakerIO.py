from .models import AProject

import json


class IcebreakerIO:
    def __init__(self, aProjectPath=None, aProjectFileName="antarcticaProject.json"):
        self.aProjectPath = aProjectPath
        self.aProjectFileName = aProjectFileName

        # print("AProject file address:", self.aProjectPath+self.aProjectFileName)

    def readAProject(self):
        with open(self.aProjectPath+self.aProjectFileName, "r") as file:
            aProjectJSON = json.load(file)

        if not aProjectJSON.get("antarctica") == "opensource":
            return -1

        aProject = AProject(path=self.aProjectPath,
                            aVersion=aProjectJSON.get("aVersion"),
                            directoryOfConfigs=aProjectJSON.get("pathToCfg"))
        aProject.parseMachinesFromJsonList(aProjectJSON.get("machines"))

        return aProject

    def readAConfig(self, aConfig):
        with open(aConfig.getAddressAConfigFile(), "r") as file:
            bodyAConfig = file.read()

        return bodyAConfig
