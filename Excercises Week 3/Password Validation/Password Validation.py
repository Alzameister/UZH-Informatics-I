#!/usr/bin/env python3

#from curses.ascii import isalpha, islower


pwd = "aaAA00++#"


def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.
    validity = False

    upperCase_Count = 0
    lowerCase_Count = 0
    number_Count = 0
    special_Chars_Count = 0
    special_Characters_Pool = ["+", "-", "*", "/"]

    pwd_length = len(pwd)

    for character in pwd:
        if character.isalpha():
            if character.isupper():
                upperCase_Count += 1
            elif character.islower():
                lowerCase_Count += 1
        elif character.isdigit():
            number_Count += 1
        elif character in special_Characters_Pool:
            special_Chars_Count += 1
        else:
            validity = False
            return validity
    
    if upperCase_Count >= 2 and lowerCase_Count >= 2 and number_Count >= 2 and special_Chars_Count >= 2 and 8 <= pwd_length <= 16:
        validity = True
    
    print(upperCase_Count)
    print(lowerCase_Count)
    print(number_Count)
    print(special_Chars_Count)
    

    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())

