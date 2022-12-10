#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    # implement this function
    #invert({"a": 1, "b": 1, "c": 3}) should return {1: ["a", "b"], 3: ["c"]}
    new_d = {}

    for key, value in d.items():
        if value not in new_d:
            #New Key with empty list as values
            new_d[value] = []
        new_d[value].append(key)
        new_d[value].sort()
    print(new_d)

    return new_d

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"b":1, "a":1, "c":3, "d": 3, "e":23.0, 4: "c"}))
