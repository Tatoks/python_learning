# Python does not support switch statements, instead we are provided with switcher

# The Pythonic way to implement switch statement is to use the powerful dictionary mappings,
# also known as associative arrays, that provide simple one-to-one key-value mappings.

# Create a dictionary named switcher to store all the switch-like cases.


def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(argument, "Invalid month")


# when you pass an argument to the switch_demo function, it is looked up against the switcher dictionary mapping.
# If a match is found, the associated value is printed, else a default string (‘Invalid Month’) is printed.
# The default string helps implement the ‘default case’ of a switch statement.
