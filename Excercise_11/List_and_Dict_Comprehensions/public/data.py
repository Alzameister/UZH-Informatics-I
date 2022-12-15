#!/usr/bin/env python3

path = r"resource/words.txt"
print(path)
with open(path) as f:
    words = f.read().splitlines()
