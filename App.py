import sys
import string
import os
import shutil
import json


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


def use_comparison():
    x = [100]
    y = [x, 100]
    z = [100]

    # check for reference
    if x is z:
        print("z: true - same object")
    else:
        print("z: false - not same object")

    # check for value
    if x == z:
        print("z: true - same value")
    else:
        print("z: false - not same value")

    # check for reference
    if x is y:
        print("y: true - same object")
    else:
        print("y: false - not same object")

    # check for value
    if x == y:
        print("y: true - same value")
    else:
        print("y: false - not same value")


def use_file_system_operations():
    # path basics
    absolute_current_working_dir = os.getcwd()
    print(os.getcwd())           # /Users/kaba/Projects/python3-playground
    print(os.curdir)             # always use 'curdir' instead of '.'
    print(os.pardir)             # always use 'pardir' instead of '..'
    print(os.listdir(os.curdir)) # ['.git', '.gitignore', '.idea', 'App.py', 'python3-playground.iml', 'test', ...]

    # dealing with paths in a platform unspecific way
    target_dir = "dir0"                          # test/dir0
    text_file = "file0.txt"                      # test/dir0/file0.txt

    # join a path
    print(os.sep)                                # always use 'path' instead of '/' or '\' -> always use 'os.path.join'
    absolute_target_dir = os.path.join(os.getcwd(), "test", target_dir)
    print(absolute_target_dir)                   # /Users/kaba/Projects/python3-playground/test/dir0
    print(os.path.isdir(absolute_target_dir))

    # split a path
    print(os.path.split(absolute_target_dir))    # ('/Users/kaba/Projects/python3-playground', 'dir0') as tuple
    print(os.path.dirname(absolute_target_dir))  # /Users/kaba/Projects/python3-playground
    print(os.path.basename(absolute_target_dir)) # dir0

    # file extensions
    absolute_text_file_path = os.path.join(os.getcwd(), target_dir, text_file)
    print(absolute_text_file_path)                    # /Users/kaba/Projects/python3-playground/test/dir0/file0.txt
    print(os.path.splitext(absolute_text_file_path))  # ('/Users/kaba/Projects/python3-playground/test/dir0/file0', '.txt')

    # most important status info
    # os.path.exists()    # TRUE for existing path or file descriptor
    # os.path.isfile()    # TRUE for existing file and symbolic link (cause it follows the link)
    # os.path.islink()    # TRUE for existing symbolic link, always false if runtime does not support symbolic links
    # os.path.isdir()     # TRUE for existing directory and symbolic link (cause it follows the link)
    # os.path.ismount()   # TRUE if 'path' is a point in a file system where a different file system has been mounted
    # os.path.isabs()     # TRUE if 'path' begins with a slash

    # os.stat()           # Get detail status information of a file or a file descriptor. See docs for details.
    # os.path.getsize()   # Get size of the file in bytes, see docs for symbolic links
    # os.path.getctime()  # Get most recent metadata change on Unix, creation on Windows in seconds
    # os.path.getatime()  # Get most recent access in seconds
    # os.path.getmtime()  # Get most recent content modification in seconds

    # rename
    # os.rename()      # Renames a file or directory

    # delete
    # os.remove()      # Deletes a file
    # os.rmdir()       # Deletes a directory, only works when the directory is empty
    # shutil.rmtree()  # Delete an entire directory tree

    # copy
    # shutil.copy()      # Copies the file src to the file/directory dst. src and dst should be strings.
    # shutil.copystat()  # Copies metadata like the permission bits, last access time, last modification time, and flags from src to dst.
    # shutil.copy2()     # Like copy() but also attempts to preserve all file metadata.
    # shutil.copytree()  # Recursively copy an entire directory tree rooted at src, returning the destination directory.

    # iterate
    # os.chdir()        # Change the current working directory to path.
    # os.walk()         # See details in the docs

    # iterate example
    print("--- os.walk example ---")
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), "test")):
        print("root: '{root}'".format(root=root))
        print("dirs: '{dirs}'".format(dirs=str(dirs)))
        print("files: '{files}'".format(files=str(files)))


def get_value_from_dict(key, dict):
    result = None
    if key in dict:
        result = dict[key]
    return result


def read_values_from_json_file():
    read_file_path = os.path.join(os.getcwd(), "test", "read.json")
    read_file_object = open(read_file_path, "r")
    file_content_as_string = "".join(read_file_object.readlines())
    file_content_as_dictionary = json.loads(file_content_as_string)

    # data structure
    first_name = get_value_from_dict("firstname", file_content_as_dictionary)
    last_name = get_value_from_dict("lastname", file_content_as_dictionary)
    age = get_value_from_dict("age", file_content_as_dictionary)

    # print results
    print("""firstname: '{firstname}', lastname: '{lastname}', age: '{age}'""".format(firstname=first_name, lastname=last_name, age=age))



def main():
    # use_for_loops()
    # use_range_function()
    # use_comparison()
    # use_file_system_operations()
    read_values_from_json_file()


main()
