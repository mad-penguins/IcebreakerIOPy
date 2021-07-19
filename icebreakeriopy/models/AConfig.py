import hashlib
from os.path import join


class AConfig:
    def __init__(self, name=None, path=None,
                 parentAMachine=None, parentARepo=None, parentAPacket=None):
        self.name = name
        self.path = path

        self.parentAMachine = parentAMachine
        self.parentARepo = parentARepo
        self.parentAPacket = parentAPacket

    def getHash(self):
        address = self.path + self.name
        return hashlib.sha224(address.encode('utf-8')).hexdigest()[:6]

    def getAddressAConfigFile(self):
        address = join(self.parentAMachine.parentAProject.path,
                       self.parentAMachine.parentAProject.directoryOfConfigs,
                       self.parentAMachine.name,
                       self.name)
        return address + " -{0}-".format(self.getHash())
