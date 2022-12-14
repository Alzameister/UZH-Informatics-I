#!/usr/bin/env python3

from gettext import find
from operator import index


s = "aB:cD"

# perform the transformation
def transform_string():
    # Insert your code here.
    # You may want to use several variables to
    # store temporary values (such as the index of
    # the colon or the two strings before and after
    # it). Then, you can construct the final result
    # from your temporary variables.
    string_length = len(s)
    index_semicolon = s.find(":")
    first_lowercase_character = 0
    first_uppercase_character = index_semicolon + 1

    s_lowercase = s[first_lowercase_character:index_semicolon]
    s_lowercase = s_lowercase.lower()
    s_uppercase = s[first_uppercase_character:string_length]
    s_uppercase = s_uppercase.upper()

    res = f"{s_lowercase}:{s_uppercase}"

    # You don't need to change the following line.
    # It simply returns the string created above.
    return res

# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(transform_string())
print() # extra newline at the end
