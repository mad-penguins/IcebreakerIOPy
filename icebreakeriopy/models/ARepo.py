from .APacket import APacket
from .AConfig import AConfig


class ARepo:
    def __init__(self, name=None, address=None, packets=None, configs=None):
        self.__name = name
        self.__address = address

        if type(packets) != list:
            self.__packets = []
        else:
            self.__packets = packets

        if type(configs) != list:
            self.__configs = []
        else:
            self.__configs = configs

    def parsePacketsFromJsonList(self, packets):
        if type(packets) == list:
            for packetJSON in packets:
                aPacket = APacket(name=packetJSON.get("name"),
                                  version=packetJSON.get("version"))
                aPacket.parseConfigsFromJsonList(packetJSON.get("configs"))
                self.__packets.append(aPacket)

    def parseConfigsFromJsonList(self, configs):
        if type(configs) == list:
            for configJSON in configs:
                aConfig = AConfig(name=configJSON.get("name"),
                                  path=configJSON.get("path"))
                self.__configs.append(aConfig)

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_packets(self):
        return self.__packets

    def get_configs(self):
        return self.__configs
