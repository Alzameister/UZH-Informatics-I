#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def req_steps(num_disks, tower_Start, tower_Goal, tower_Spare):
    # implement this function
        tower_Start = range(1,num_disks)
        tower_Goal = []
        tower_Spare = []

        if num_disks == 1:
            return 1
        
        req_steps(num_disks-1, tower_Start, tower_Spare, tower_Goal)

        req_steps(num_disks-1, tower_Spare, tower_Goal, tower_Start)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(3, req_steps(3,1,2,3)))

