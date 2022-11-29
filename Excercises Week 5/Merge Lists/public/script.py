#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

from operator import le
from queue import Empty


def merge(a, b):
    merge_list = []

    #Return empty list if one of the 2 input lists are empty
    if not a or not b:
        return merge_list
    
    if len(a) > len(b):
        #Append last digit of b to b until length of b reaches a
        for index in range(len(a) - len(b)):
            b.append(b[-1])
    elif len(a) < len(b):
        for index in range(len(b) - len(a)):
            a.append(a[-1])

    return list(zip(a,b))



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0,2,3,4,5,5,6,1], [1,2]))
