#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num_words = 7
length = 4
attempts = 4

with open("words.txt") as f:
  word_list = f.read().splitlines()

fixed_length_words = [word.upper() for word in word_list if len(word) is length]

import random

random.shuffle(fixed_length_words)
words = fixed_length_words[0:num_words]
password = random.choice(words)

print(" ".join(words))

while attempts != 0:
    guess = input("> ").upper()
    if len(guess) != length:
        print("Wrong length")
        continue
    if guess == password:
        print("Access granted!")
        break
    else:
        matching = 0
        for i in range(length):
            if guess[i] == password[i]: matching += 1
        print("%d/%d correct" % (matching, length))
        print("Access denied!")
        attempts = attempts - 1
        print("%s attempts remaining..." % attempts)

