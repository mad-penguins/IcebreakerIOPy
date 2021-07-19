from .ARepo import ARepo
from .AConfig import AConfig


class AMachine:
    def __init__(self, name=None, repos=None, configs=None,
                 parentAProject=None):
        self.name = name

        if type(repos) != list:
            self.repos = []
        else:
            self.repos = repos

        if type(configs) != list:
            self.configs = []
        else:
            self.configs = configs

        self.parentAProject = parentAProject

    def parseReposFromJsonList(self, repos):
        if type(repos) == list:
            for repoJSON in repos:
                aRepo = ARepo(name=repoJSON.get("name"),
                              address=repoJSON.get("address"),
                              parentAMachine=self)

                aRepo.parsePacketsFromJsonList(repoJSON.get("packets"))
                aRepo.parseConfigsFromJsonList(repoJSON.get("configs"))

                self.repos.append(aRepo)

    def parseConfigsFromJsonList(self, configs):
        if type(configs) == list:
            for configJSON in configs:
                aConfig = AConfig(name=configJSON.get("name"),
                                  path=configJSON.get("path"),
                                  parentAMachine=self)
                self.configs.append(aConfig)
