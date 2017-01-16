class Settings(object):
    def __init__(self):
        self.__read_par()

    def __read_par(self):
        with open("..\data\settings.properties") as f:
            for line in f:
                lst = line.split(" ")
                if lst[0] == "repository":
                    self.__repomode = lst[2].strip("\n").strip("\"")
                elif lst[0] == "persons":
                    self.__persons = lst[2].strip("\n").strip("\"")
                elif lst[0] == "activities":
                    self.__activities = lst[2].strip("\n").strip("\"")
                elif lst[0] == "appointments":
                    self.__appointments = lst[2].strip("\n").strip("\"")

    @property
    def repo_mode(self):
        return self.__repomode

    @property
    def activity_repo(self):
        return self.__activities

    @property
    def persons_repo(self):
        return self.__persons

    @property
    def apppoinment_repo(self):
        return self.__appointments