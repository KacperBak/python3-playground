from animal import Animal
from abc import ABC, abstractmethod


class Dog(Animal):

    # A constructor with default values
    def __init__(self, name=None, dsc=None, legs=4):
        super(Dog, self).__init__(name, dsc)
        self.legs = legs

    # A user defined string representation of the object. Implement __repr__ for a more strict one.
    def __str__(self):
        return """name: '{n}', description: '{d}', legs: '{l}'""".format(n=self.name, d=self.description, l=self.legs)

    @staticmethod
    def animal_code():
        return "0001"

