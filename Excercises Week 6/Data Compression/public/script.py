#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
from optparse import Values
from typing import KeysView


def compress(data):
    key_list = []
    key_tuple = ()
    value_list = []

    #Check if Input is empty
    if len(data) == 0:
        return key_tuple, value_list

    #Get keys and put them into a list
    for dict in data:
        for key in dict.keys():
            key_list.append(key)

    #Remove duplicate keys from the list, sort and transform to tuple
    key_list = list(dict.fromkeys(key_list))
    key_list.sort()
    key_tuple = tuple(key_list)
    
    #Add values in order to list --> Has to be values in order of the sorted keys
    for dict in data:
        value_temp_list = []
        for key in key_tuple:
            for keys, values in dict.items():
                if key == keys:
                    value_temp_list.append(values)

        value_tuple = tuple(value_temp_list)
        value_list.append(value_tuple)

    return key_tuple, value_list

    

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"c": 9, "a": 7, "b": 8}
]
print(compress(data))