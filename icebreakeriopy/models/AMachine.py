from .ARepo import ARepo


class AMachine:
    def __init__(self, name=None, repos=None):
        self.__name = name

        if type(repos) != list:
            self.__repos = []
        else:
            self.__repos = repos

    def parseReposFromJsonList(self, repos):
        if type(repos) == list:
            for repoJSON in repos:
                aRepo = ARepo(name=repoJSON.get("name"),
                              address=repoJSON.get("address"))

                aRepo.parsePacketsFromJsonList(repoJSON.get("packets"))
                aRepo.parseConfigsFromJsonList(repoJSON.get("configs"))

                self.__repos.append(aRepo)

    def get_name(self):
        return self.__name

    def get_repos(self):
        return self.__repos
