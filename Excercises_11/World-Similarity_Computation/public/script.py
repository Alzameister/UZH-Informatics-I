#!/usr/bin/env python3

import random
from math import floor
from difflib import SequenceMatcher

class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)

        # TODO: instead of returning a random sample of words, use the strategy described in task 2
        sel_words = [words[i] for i in range(floor(self.num_words/3))]
        print(sel_words)
        while len(sel_words) < self.num_words:
            sel = random.choice(words)
            if self.is_similar(random.choice(sel_words), sel, 0.4) and sel not in sel_words:
                sel_words.append(sel)

        return sel_words

    def is_similar(self, a, b, threshold):
        matching = SequenceMatcher(None, a, b).ratio()
        print(matching)
        if matching > threshold:
            return True
        return False