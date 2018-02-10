from animal import Animal
from dog import Dog, Bernard
from bird import Bird


def basics():
    # failing to instantiate an class with '@abstractmothods'
    # animal = Animal()
    # print(animal)

    # instantiate Dog
    default_dog = Dog()
    snoop_dog = Dog("Snoop", "A dog that smokes a lot", 2)
    booze_dog = Bernard("Johnnie Walker", "St Bernard with the iconic barrel", barrelvolume=1)

    # instantiate Bird
    default_bird = Bird()
    bird_of_prey = Bird("Bird-of-Prey", "An agile Klingon starship")

    # print results
    print(default_dog)
    print(snoop_dog)
    print(booze_dog)
    print(default_bird)
    print(bird_of_prey)