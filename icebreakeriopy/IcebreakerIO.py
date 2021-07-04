from .models import AProject

import json


class IcebreakerIO:
    def __init__(self, aProjectFileAddress=None):
        self.aProjectFileAddress = aProjectFileAddress

        print("AProject file address:", self.aProjectFileAddress)

    def readAProject(self):
        with open(self.aProjectFileAddress, "r") as file:
            aProjectJSON = json.load(file)

        if not aProjectJSON.get("antarctica") == "opensource":
            return -1

        aProject = AProject(aVersion=aProjectJSON.get("aVersion"),
                            pathToCfg=aProjectJSON.get("pathToCfg"))
        aProject.parseMachinesFromJsonList(aProjectJSON.get("machines"))

        return aProject
