from abc import ABC, abstractmethod


class Log(ABC):

    __instance = None

    @staticmethod
    def get_instance():
        """ Singleton """
        if Log.__instance is None:
            Log.__instance = Log()
        return Log.__instance

    def __init__(self, level="debug"):
        self.level = level

    def __str__(self):
        return """level: '{lvl}'""".format(lvl=self.level)