#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
plain_text = "abzAZ!"
shift_by = 26

# perform a ROTn encoding
def rot_n():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    changed_text = ""
    for c in plain_text:
        if shift_by > 0:
            if c.isalpha() and c.isupper():
                ascii = ord(c)
                ascii += shift_by
                c = chr(ascii)

                if ascii > 90:
                    ascii -= 26
                    c = chr(ascii)
            
            if c.isalpha() and c.islower():
                ascii = ord(c)
                ascii += shift_by
                c = chr(ascii)

                if ascii > 122:
                    ascii -= 26
                    c  = chr(ascii)
            
        if shift_by < 0:
            if c.isalpha() and c.isupper():
                ascii = ord(c)
                ascii += shift_by
                c = chr(ascii)

                if ascii < 65:
                    ascii += 26
                    c = chr(ascii)
            
            if c.isalpha() and c.islower():
                ascii = ord(c)
                ascii += shift_by
                c = chr(ascii)

                if ascii < 97:
                    ascii += 26
                    c = chr(ascii)

        changed_text = changed_text + f"{c}"
    
    encoded = changed_text

    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded
    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())

