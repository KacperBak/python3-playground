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


def use_dictionary():
    dict = {}
    dict[0] = 0
    dict["one"] = "one"
    dict["two"] = "two"
    dict[3] = "three"
    print("size of the dictionary: " + str(len(dict)))
    for value in dict.values():
        print(value)


def use_dictionary_with_frozenset():
    # create keys
    kacperbak = frozenset({"Kacper", "Bak"})
    michaelmayer = frozenset({"Michael", "Mayer"})
    stefandaum = frozenset({"Stefan", "Daum"})

    # create dictionary
    phonebook = {kacperbak : "0821-123", michaelmayer : "0821-456", stefandaum : "0821-789"}

    # test
    print(phonebook.get(kacperbak))

    # test with default result
    olafmaier = frozenset({"Olaf", "Maier"})
    defaultresult = phonebook.get(olafmaier, "0815")
    print(defaultresult)
    print("Is Olaf part of the phonebook?: {ispart}".format(ispart=(olafmaier in phonebook)))

    # test with setdefault result
    setdefaultresult = phonebook.setdefault(olafmaier, "0815")
    print(setdefaultresult)
    print("Is Olaf part of the phonebook?: {ispart}".format(ispart=(olafmaier in phonebook)))


def use_range_function():
    # create a list using the range function
    two_step_list = list(range(0, 10, 2))
    print("two step list: " + str(two_step_list))

    # for loop with indices using the range function
    for index in range(10):
        print("index: " + str(index))

    # for loop with indices using the range function over a collection
    for index in range(len(two_step_list)):
        print("""index: '{index}' value: '{value}'""".format(index=index, value=two_step_list[index]))


def use_for_loops():
    tuple_list = [(1,2),(3,4),(5,6)]
    result0 = 0
    result1 = 0

    # sum up tuples with index
    for t in tuple_list:
        result0 = result0 + (t[0] * t[1])

    # sum up tuples with named parameters
    for x, y in tuple_list:
        result1 = result1 + (x * y)

    # print both results
    print("""result0: '{result0}' result1: '{result1}'""".format(result0=result0, result1=result1))

    # use the 'enumerate' function: it return the items of the list as tuples
    list_0 = [100, 200, 300, 400]
    enumeration = enumerate(list_0) # (1, 100), (2, 200) ...
    for index, value in enumeration:
        print("""index: '{index}', value: '{value}'""".format(index=index, value=value))

    # use the zip function to combine two lists as one tupled list
    list_a = ['a', 'b', 'c']
    zipped_list = zip(list_a, list_0)
    for a, b in zipped_list:
        print("""a: '{a}', b: '{b}'""".format(a=a, b=b))


def main():
    use_for_loops()
    use_range_function()


main()
