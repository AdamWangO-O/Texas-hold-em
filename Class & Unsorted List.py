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

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def displayCard(self):  # Display suit and number
        print("Suit:", self.suit, "Number:", self.number)


# Get the deck with 52 cards:
Deck = []

for suit in Card.suits:
    for number in Card.numbers:
        card = Card(suit, number)
        Deck.append(card)

# Full unsorted list of 5 cards from the deck:
unsorted_list_5 = list(combinations(Deck, 5))
test_list = unsorted_list_5 [0:2]
with open("test.pkl", 'wb') as file:
    pickle.dump(test_list,file)

with (open("test.pkl", "rb")) as openfile:
    new_list = pickle.load(openfile)

print(new_list[0][0].number)
