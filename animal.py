from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, name=None, dsc=None):
        self.name = name
        self.description = dsc

    @abstractmethod
    def __str__(self):
        pass

    @staticmethod
    @abstractmethod
    def animal_code():
        pass

