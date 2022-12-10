#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
from queue import Empty


def min_domino_rotations(top, bottom):
    number = 1
    solvable = False
    number_to_solve = -1
    rotation_counter = 0
    top_counter = 0
    bottom_counter = 0


    #Create tuples of domino stones 
    domino_stones = list(zip(top, bottom))

    #Check if every tuple contains the same number --> If yes, problem solvable
    while number <= 9:
        solvable_stones = 0
        for tuple in domino_stones:
            if (number in tuple):
                solvable_stones += 1
        
        if solvable_stones == len(top) and solvable_stones == len(bottom):
            solvable = True
            number_to_solve = number
        
        number += 1

    if (solvable):
        #Check if top or bottom contains more of the number_to_solve
        for index in range(len(top)):
            if top[index] is number_to_solve:
                top_counter += 1
            if bottom[index] is number_to_solve:
                bottom_counter += 1
        print(f"Top Counter: {top_counter}")
        print(f"Bottom Counter: {bottom_counter}")

        #Rotate dominos to top or bottom depending who has more of number_to_solve
        #Rotate to Top
        if top_counter > bottom_counter:
            for index in range(len(top)):
                if top[index] is not number_to_solve:
                    (top[index], bottom[index]) = (bottom[index], top[index])
                    rotation_counter+=1
        #Rotate to bottom
        else:
            for index in range(len(bottom)):
                if bottom[index] is not number_to_solve:
                    (top[index], bottom[index]) = (bottom[index], top[index])
                    rotation_counter+=1
        return rotation_counter
    return -1


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 4, 1, 3, 2], [5, 2, 4, 2, 2, 2, 4]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
