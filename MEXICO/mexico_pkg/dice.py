import random


class Die:

    def __init__(self):
        self.dice = 0

    def roll(self):
        dice = random.randint(1, 6)
        return dice
