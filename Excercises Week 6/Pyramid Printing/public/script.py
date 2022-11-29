#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
from ast import If


h = 7

# build a string 
def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""
    line_number = ""
    # Enter your code here
    # use nested loops and the range() function
    
    #add ascending half of the pyramid
    for number in range(1, h+1):
        s += line_number + str(number) + "\n"
        line_number += str(number) + "*"
    
    #Creates list of all lines
    half_pyramid = s.split("\n")
    print(half_pyramid)
    #number of lines needed: Length of half_pyramd minus 3 since the last two are not needed and index ends at 0
    line_index = len(half_pyramid) - 3

    #Add the declining half of the pyramid
    for i in range(h):
        s += str(half_pyramid[line_index]) + "\n"
        line_index += -1
    s = s.strip()

    # You don't need to change the following line.
    # It simply returns the string created above.
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



