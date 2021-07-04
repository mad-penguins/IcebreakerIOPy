class AConfig:
    def __init__(self, name=None, path=None):
        self.__name = name
        self.__path = path

    def get_name(self):
        return self.__name

    def get_path(self):
        return self.__path
