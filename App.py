import sys


def execute_triple_quoted_string():
    triple_qutoed_string = """"Hello" world'!'"""
    print(triple_qutoed_string)


def use_input_and_output():
    input_as_int = int(input("Please type in a number: "))
    print(input_as_int)


def main():
    execute_triple_quoted_string()
    use_input_and_output()

    # arg0 = sys.argv[0]
    # arg1 = sys.argv[1]
    # print("0 argument: " + arg0)
    # print("1st argument: " + arg1)
 


main()
