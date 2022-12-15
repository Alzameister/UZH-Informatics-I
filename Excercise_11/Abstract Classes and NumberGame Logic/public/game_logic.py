#!/usr/bin/env python3

# TODO: Implement Me
import os
from random import choice, shuffle
from abc import ABC, abstractmethod

class GameLogic(ABC):
    def __init__(self, num_words, len_words, num_attempts):
        """Set up a new game with the provided parameters"""
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        self.words = self._word_selection()
        self.password = choice(self.words)

    def check(self, guess):
        """Check a guess and give feedback"""
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            return False, [self._generate_feedback(guess), "Access denied!"]

    @abstractmethod
    def _word_selection():
        pass

    @abstractmethod
    def _generate_feedback():
        pass