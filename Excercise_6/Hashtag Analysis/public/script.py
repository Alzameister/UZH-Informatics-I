#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters
from unicodedata import numeric


def analyze(posts):
    hashtag_dict = {}
    list_of_strings = []

    for strings in posts:
        list_of_strings = strings.split(" ")
        for words in list_of_strings:
            if "#" in words:
                if len(words) > 1:
                    if words[1].isalpha():
                        if words[1:] not in hashtag_dict:
                            hashtag_dict[words[1:]] = 0
                        if words[1:] in hashtag_dict:
                            hashtag_dict[words[1:]] += 1
    
    return hashtag_dict

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend .#c.",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
