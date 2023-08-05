#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from itertools import combinations
import pandas as pd
import pickle

# Define a Card class including suit and number:
class Card:
    def __eq__(self, other):
        if (self.suit == other.suit) and (self.number == other.number):
            return True
        else:
            return False

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def displayCard(self):  # Display suit and number
        print("Suit:", self.suit, "Number:", self.number)
