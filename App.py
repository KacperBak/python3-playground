import sys
import string

def use_triple_quoted_string():
    triple_qutoed_string = """"Hello" world'!'"""
    print(triple_qutoed_string)


def use_input_and_output():
    input_as_int = int(input("Please type in a number: "))
    print(input_as_int)


def use_intersection():
    set0 = {1, 2, 3}
    list0 = [2, 3, 4]
    set1 = set(list0)
    print(set0 & set1)


def use_passed_arguments(args):
    number_of_passed_arguments = len(args)
    print("Number of passed arguments: " + str(number_of_passed_arguments))
    for arg in args:
        print(arg)


def use_remove_all_whitespace():
    # Print input_string
    input_string = "          - Before -\tMiddle\t- End -        "
    print("Raw input:" + input_string)

    # Escape whitespaces on start and on the end
    print("strip:" + input_string.strip())

    # Escape whitespaces on start, end and in the middle
    for character in string.whitespace:
        input_string = input_string.replace(character, "")
    print("replace:" + input_string)


def use_repr_method():
    # Create an object of type list
    x = [1,2,3]

    # Convert the object to a string
    str0 = "This is my list: " + repr(x)

    print(str0)


def use_format_parameter():
    positional_parameter_string = """'{0}' is the food of user '{1}'""".format("Steak", "Kacper")
    named_parameter_string = """'{food}' is the food of user '{user}'""".format(food="Steak", user="Kacper")
    print(positional_parameter_string)
    print(named_parameter_string)


def main():
    use_format_parameter()


main()
