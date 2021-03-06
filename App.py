import procstuff
import oopstuff
import libstuff
from log import *

def main():

    ##############################
    # play with procedural stuff #
    ##############################

    # use_for_loops()
    # use_range_function()
    # use_comparison()
    # use_file_system_operations()
    # stuff.use_assert_statement(None)

    # read/write JSON file
    # data_file_path = os.path.join(os.getcwd(), "test", "read_write_json", "data.json")
    # write_values_to_json_file(data_file_path)
    # read_values_from_json_file(data_file_path)

    # print(use_var_args_as_tuple(1, 2, 3))
    # use_var_args_as_dict("x-one", "y-one", z1="z-one", z2="z-two", z3="z-three")
    # jinja2_template_usage()
    # print(procstuff.cat_file())
    # print(procstuff.datetime_now_formatted())
    # print(procstuff.get_interface_inet('en0'))
    procstuff.recursive_file_walk()

    #######################
    # play with oop stuff #
    #######################
    # oopstuff.basics()

    #######################
    # play with lib stuff #
    #######################
    # libstuff.post_to_mailgun_api()


main()
