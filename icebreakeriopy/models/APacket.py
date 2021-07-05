from .AConfig import AConfig


class APacket:
    def __init__(self, name=None, version=None, configs=None):
        self.name = name
        self.version = version

        if type(configs) != list:
            self.configs = []
        else:
            self.configs = configs

    def parseConfigsFromJsonList(self, configs):
        if type(configs) == list:
            for configJSON in configs:
                aConfig = AConfig(name=configJSON.get("name"),
                                  path=configJSON.get("path"))
                self.configs.append(aConfig)
