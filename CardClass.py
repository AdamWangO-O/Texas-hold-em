#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from itertools import combinations
import pandas as pd
import pickle

# Define a Card class including suit and number:
class Card:
    suits = ['S', 'H', 'D', 'C']  # Spade, Heart, Diamond, Club
    numbers = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def __eq__(self, other):
        if (self.suits == other.suits) and (self.numbers == other.numbers):
            return True
        else:
            return False

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def displayCard(self):  # Display suit and number
        print("Suit:", self.suit, "Number:", self.number)
