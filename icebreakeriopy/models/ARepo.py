from .APacket import APacket
from .AConfig import AConfig


class ARepo:
    def __init__(self, name=None, address=None, packets=None, configs=None,
                 parentAMachine=None):
        self.name = name
        self.address = address

        if type(packets) != list:
            self.packets = []
        else:
            self.packets = packets

        if type(configs) != list:
            self.configs = []
        else:
            self.configs = configs

        self.parentAMachine = parentAMachine

    def parsePacketsFromJsonList(self, packets):
        if type(packets) == list:
            for packetJSON in packets:
                aPacket = APacket(name=packetJSON.get("name"),
                                  version=packetJSON.get("version"),
                                  parentARepo=self)
                aPacket.parseConfigsFromJsonList(packetJSON.get("configs"))
                self.packets.append(aPacket)

    def parseConfigsFromJsonList(self, configs):
        if type(configs) == list:
            for configJSON in configs:
                aConfig = AConfig(name=configJSON.get("name"),
                                  path=configJSON.get("path"),
                                  parentAMachine=self.parentAMachine,
                                  parentARepo=self)
                self.configs.append(aConfig)
