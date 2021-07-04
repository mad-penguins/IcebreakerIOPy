from .AConfig import AConfig


class APacket:
    def __init__(self, name=None, version=None, configs=None):
        self.__name = name
        self.__version = version

        if type(configs) != list:
            self.__configs = []
        else:
            self.__configs = configs

    def parseConfigsFromJsonList(self, configs):
        if type(configs) == list:
            for configJSON in configs:
                aConfig = AConfig(name=configJSON.get("name"),
                                  path=configJSON.get("path"))
                self.__configs.append(aConfig)

    def get_name(self):
        return self.__name

    def get_version(self):
        return self.__version

    def get_configs(self):
        return self.__configs
