from animal import Animal


class Bird(Animal):

    # A constructor with default values
    def __init__(self, name=None, dsc=None, wings=2):
        super(Bird, self).__init__(name, dsc)
        self.wings = wings

    # A user defined string representation of the object. Implement __repr__ for a more strict one.
    def __str__(self):
        return """name: '{n}', description: '{d}', wings: '{w}'""".format(n=self.name, d=self.description, w=self.wings)

    @staticmethod
    def animal_code():
        return "0001"

