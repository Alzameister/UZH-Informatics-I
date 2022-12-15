#!/usr/bin/env python3
from game_logic import GameLogic
from random import choice

class NumberLogic(GameLogic):
    def _word_selection(self):
        numbers = []
        for _ in range(self.num_words):
            available_nrs = [1,2,3,4,5,6,7,8,9,0]
            seq = ""
            for _ in range(self.len_words):
                in_numbers = True
                while in_numbers:
                    rand_nr = choice(available_nrs)
                    if rand_nr in available_nrs:
                        seq = seq + str(rand_nr)
                        available_nrs.remove(rand_nr)
                        in_numbers = False
            numbers.append(seq)
        return numbers
    
    #TODO: Check and Generate feedback method
    def check(self, guess):
        pass

    def _generate_feedback():
        pass
    
Nl = NumberLogic(4,5,4)
print(Nl._word_selection())