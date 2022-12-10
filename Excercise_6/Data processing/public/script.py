#!/usr/bin/env python3

from importlib.resources import path
from operator import contains
import os
from pickletools import read_stringnl_noescape
import sys

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        return False
    # the rest of your implementation
    #Open .txt files
    output_file = open(path_writing, "w")
    input_file = open(path_reading, "r")

    #Check if there is only one line with "Name"

    for line in input_file.readlines():
        line_words = ""
        #Write headers onto output
        if line == "Name":
            output_file.write("Fristname,Lastname")
        if line == "Name\n":
            output_file.write("Firstname,Lastname\n")
        
        #Split lines into Firstname and Lastname
        if line.__contains__(" "):
            line_words = line.split(" ")
        if line.__contains__(";"):
            line_words = line.split(";")
            line_words.reverse()
        #Invert \n for names with ";"
            if line_words[0].__contains__("\n"):
                print(line_words[0])
                line_words[0] = line_words[0].replace("\n", "")
                line_words[1] = line_words[1] + "\n"
        
        #Delete spaces
        for index in range(line_words.__len__()):
            line_words[index] = line_words[index].replace(" ", "")


        #Add names to output
        if line == "\n":
            output_file.write(",\n")
        elif line_words:
            output_file.write(f"{line_words[0]},{line_words[1]}")

    output_file.close()

# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = os.path.join(sys.path[0], "my_data.txt")
#"public/my_data.txt"
OUTPUT_PATH = os.path.join(sys.path[0], "my_data_processed.txt")
#"public/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)


if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

