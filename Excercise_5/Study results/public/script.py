#!/usr/bin/env python3

import os
from pathlib import Path

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    grades = [] 
    final_grade = 0

    if not os.path.exists(path):
        return None
    
    f = open(path, "r")
    
    #Go through all lines in the document and extract grades
    for line in f.readlines():

        #If line is not empty, extract grade and convert to float
        line = line[:-1]

        if line.strip():
            if line[0] != "#":
                #Check if theres a character after the ":" and then add to grades
                if line.split(":", 1)[1]:
                    grades.append(float(line.split(":", 1)[1]))
                    print(line)

    if len(grades) > 0:
        final_grade = sum(grades) / len(grades)
        return final_grade
    else: 
        return 0.0


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
filepath = Path(__file__).parent / "my_grades.txt"
print(get_average_grade(filepath))

