from .AConfig import AConfig


class APacket:
    def __init__(self, name=None, version=None, configs=None,
                 parentARepo=None):
        self.name = name
        self.version = version

        if type(configs) != list:
            self.configs = []
        else:
            self.configs = configs

        self.parentARepo = parentARepo

    def parseConfigsFromJsonList(self, configs):
        if type(configs) == list:
            for configJSON in configs:
                aConfig = AConfig(name=configJSON.get("name"),
                                  path=configJSON.get("path"),
                                  parentAMachine=self.parentARepo.parentAMachine,
                                  parentARepo=self.parentARepo,
                                  parentAPacket=self)
                self.configs.append(aConfig)
