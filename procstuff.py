import sys
import string
import os
import shutil
import json
import subprocess
import pytz
import datetime
import jinja2

def use_split_on_string():
    input = "first-second-third"
    result = input.split("-")
    assert result[0] == "first"
    assert result[1] == "second"
    assert result[2] == "third"

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

    # handle not present key in dict
    none = dict.get("nothing")
    assert none is None

    # handle not present key in dict with 'default' value
    default = dict.get("nothing", "default")
    assert default == "default"


def use_assert_statement(something):
    debug_value = __debug__
    print("""System variable '__debug__':'{v}'""".format(v=debug_value))

    assert something is not None
    assert len(str(something)) > 0


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


def get_abs_parent_dir(your_path):
    return os.path.abspath(os.path.join(your_path, os.pardir))


def get_value_from_dict(key, dict):
    result = None
    if key in dict:
        result = dict[key]
    return result


def read_values_from_json_file(file_path):
    assert len(str(file_path)) > 0
    read_file_object = open(file_path, "r")
    file_content_as_string = "".join(read_file_object.readlines())
    file_content_as_dictionary = json.loads(file_content_as_string)
    read_file_object.close()

    # data structure
    first_name = file_content_as_dictionary.get("first_name")
    last_name = file_content_as_dictionary.get("last_name")
    age = file_content_as_dictionary.get("age")

    # print results
    print("""first_name: '{first_name}', last_name: '{last_name}', age: '{age}'""".format(first_name=first_name, last_name=last_name, age=age))


def write_values_to_json_file(file_path):
    assert len(str(file_path)) > 0
    write_file_object = open(file_path, "w")
    json_content_as_dictionary = {"first_name": "Kacper", "last_name": "Bak", "age": 34}
    json.dump(json_content_as_dictionary, write_file_object, indent=2)
    write_file_object.close()


def use_var_args_as_tuple(*args):
    if len(args) == 0:
        return None
    else:
        result = args[0]
        for arg in args:
            if arg > result:
                result = arg
        return result


def use_var_args_as_dict(x, y, **args):
    print("""x: '{x}', y: {y}""".format(x=x, y=y))
    for key in args.keys():
        print("""key: '{key}', value: '{value}'""".format(key=key, value=args[key]))


def is_x64_architecture():
    result = False
    const_x64 = 'x86_64'
    out = subprocess.check_output(["uname", "-m"])
    out_as_str = out.decode("utf-8").strip()
    if out_as_str == const_x64:
        result = True
    return result


def execute_bash_prototype():
    script = "prototype.sh"
    subprocess.check_call(["chmod", "u+x", os.path.join(os.getcwd(), "bash", script)])
    out = subprocess.check_output([os.path.join(os.getcwd(), "bash", script)])
    out_as_str = out.decode("utf-8").strip()
    print(out_as_str)


def subprocess_with_pipe(searchstr):

    result = False
    try:
        # look in file '/python3-playground/test/dir0/file0.txt' for 'searchstr'
        cat_out = subprocess.Popen(["cat", os.path.join(os.getcwd(), "test", "dir0", "file0.txt")], stdout=subprocess.PIPE)
        grep_out = subprocess.check_output(["grep", "-w", searchstr], stdin=cat_out.stdout)

        # p1 to receive a SIGPIPE if p2 exits before p1
        # details https://docs.python.org/2/library/subprocess.html#replacing-shell-pipeline
        cat_out.stdout.close()

        grep_out_as_string = grep_out.decode('utf-8').strip()
        print(grep_out_as_string)
        if grep_out_as_string == searchstr:
            result = True

    except subprocess.CalledProcessError as cpe:
        print("""grep failed with exit code: '{c}'""".format(c=cpe.returncode))
    except:
        print("Something other gone wrong.")
    return result


def jinja2_template_usage():
    template_loader = jinja2.FileSystemLoader(searchpath=os.path.join(os.getcwd(), "jinja2"))
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("template.file")
    args = {'port': 123}
    output = template.render(args)
    print(output)


def cat_file():
    file = os.path.join(os.getcwd(), "test", "read_write_json", "data.json")
    cat_result = subprocess.check_output(["cat", file])
    return cat_result.decode('utf-8').strip()


def datetime_now():
    return str(datetime.datetime.now())


def datetime_now_formatted():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def basic_comparisons():
    ten = 10
    assert 10 > 9
    assert 10 >= 10
    assert ten >= 10


def get_interface_inet(iface):
    assert isinstance(iface, str)
    assert len(str(iface)) > 0

    # bash: ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'
    ifconfig_out = subprocess.Popen(["ifconfig", iface], stdout=subprocess.PIPE)
    return subprocess.check_output(["grep", "inet 1"], stdin=ifconfig_out.stdout).decode('utf-8').strip()
    # grep_out = subprocess.Popen(["grep", """\'inet addr:\'"""], stdin=ifconfig_out.stdout, stdout=subprocess.PIPE)
    # cut_out = subprocess.Popen(["cut", "-d:", "-f2"], stdin=grep_out.stdout, stdout=subprocess.PIPE)
    # return subprocess.check_output(["awk", "{print $1}"], stdin=cut_out.stdout).decode('Utf-8').strip()
