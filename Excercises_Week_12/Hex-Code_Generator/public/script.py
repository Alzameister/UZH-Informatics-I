#!/usr/bin/env python3
from random import choice

class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        res = []
        for i in range(self.columns):
            for j in range(self.rows):
                line = "0x"
                for _ in range(4):
                    line = line + choice("0123456789ABCDEF")
                res.append(line)
        return res
