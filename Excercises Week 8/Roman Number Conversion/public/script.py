#!/usr/bin/env python3

# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def check_valid_string(roman):
    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for char in roman:
        if char not in roman_single_digits:
            raise Warning("Invalid Input")
    return True

def check_pattern(roman):
    if len(roman) >= 4:
        for i, char in enumerate(roman):
            if i+3 < len(roman):
                if roman[i] + roman[i+1] == roman[i+2] + roman[i+3] and roman[i] != "M":
                    raise Warning("Invalid pattern")

def check_invalid_repetition(roman):
    roman_incorrect_repetitions = [
        #Cases not allowed to repeat
        "V",
        "L",
        "D"
    ]

    if len(roman) >= 2:
        for i, char in enumerate(roman):
            if i+1 < len(roman) and char in roman_incorrect_repetitions:
                if roman[i] == roman[i+1]:
                    raise Warning("Invalid repetition")


def convert_roman_to_int(roman):
    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    num = 0

    #Check if roman is valid
    check_valid_string(roman)
    check_pattern(roman)
    check_invalid_repetition(roman)

    #Go through each character and convert values
    checked_chars = []

    for idx, char in enumerate(roman):
        added_double_digit = False
        
        if idx < len(roman)-1:
            #Add double digit
            if roman[idx] + roman[idx+1] in roman_double_digits:
                double_digit = roman[idx] + roman[idx+1]
                num += roman_double_digits[double_digit]

                #Check if a valid single digit comes after the double digit

                added_double_digit = True
                checked_chars.append(idx+1)
                print(f"Added double digit, num is now: {num}")
            #Add single digit
            elif idx != len(roman)-1 and idx not in checked_chars:
                num += roman_single_digits[char]
                print(f"Added single digit, num is now: {num}")

            #Check if a valid single digit comes after double digit
            if len(roman) >= 3 and added_double_digit == True:
                #print(idx)
                if idx-1 >= 0:
                    if roman[idx+1] == roman[idx-1]:
                        raise Warning("Invalid pattern")

        #Add final digit
        else:
            num += roman_single_digits[char]
            print(f"Added final digit, num is now: {num}")

        #Break out of loop and prevent adding the single digit twice if the last 2 digits were a valid double digit
        if added_double_digit and idx == len(roman)-2:
            break

    return num


# The following lines calls the function and prints the return
# value to the Console.
i = convert_roman_to_int("IV")
print(i)

