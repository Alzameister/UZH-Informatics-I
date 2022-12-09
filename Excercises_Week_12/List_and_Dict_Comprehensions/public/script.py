#!/usr/bin/python3

from data import words
import string

def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [word for word in words if s in word]

def words_starting_with_character(c):
    return [word for word in words if word[0] == c]

def alphabet():
    '''you don't have to solve this one using a comprehension.'''
    return string.ascii_lowercase

def dictionary():
    return dict(zip([letter for letter in alphabet()], (words_starting_with_character(letter) for letter in alphabet())))

def censored_words(s):
    for word in words:
        print(word.find(s))
    return ["x"*len(word) for word in words if s in word]

print(words_containing_string("slut"))
print(censored_words("slut"))