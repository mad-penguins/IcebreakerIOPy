from .ARepo import ARepo


class AMachine:
    def __init__(self, name=None, repos=None):
        self.name = name

        if type(repos) != list:
            self.repos = []
        else:
            self.repos = repos

    def parseReposFromJsonList(self, repos):
        if type(repos) == list:
            for repoJSON in repos:
                aRepo = ARepo(name=repoJSON.get("name"),
                              address=repoJSON.get("address"))

                aRepo.parsePacketsFromJsonList(repoJSON.get("packets"))
                aRepo.parseConfigsFromJsonList(repoJSON.get("configs"))

                self.repos.append(aRepo)
