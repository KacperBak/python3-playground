import sys


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


def main():
    use_passed_arguments(sys.argv)


main()
