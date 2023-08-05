from CardClass import *
import os
import re
import pickle
Deck = []

for i in range (2,15):
    for j in ['S','H','D','C']:
        card = Card(j,i)
        Deck.append(card)
def IdCard(Card):
    pattern = r'([A-Za-z]+)(\d+)'
    matches = re.findall(pattern, Card)
    return matches

def Del_Card(sub_dir,d):
    remove = IdCard(sub_dir)
    Remove_List = []
    for i in remove:
        suit = i[0]
        number = int(i[1])
        Remove_List.append(Card(suit,number))
    return [card for card in d if card not in Remove_List]

# Cat IS SHORT FOR Catalogue
def Creat_Cat(deck):
    Base = list(combinations(deck,2))
    Org_Base = []
    for i in Base:
        Org = sorted(i, key=lambda x: (x.number,x.suit),reverse=True)
        # S > H > D > C
        Org_Base.append(Org)
    Cat = []
    for i in Org_Base:
        a = [i[0], i[1], -0.1, ""]
        Cat.append(a)
    return Cat

Cat = Creat_Cat(Deck)
for i in Cat:
    i[3] = str(i[0].suit) + str(i[0].number) + str(i[1].suit) + str(i[1].number)
    path = "D:\Texas hold em\Card_Base"
    path = os.path.join(path, i[3])
    os.mkdir(path)
    sub_dir = i[3]
    deck = Del_Card(sub_dir,Deck)
    print(len(deck))

#with open("D:\Texas hold em\Card_Base\Private.pkl", 'wb') as file:
    #pickle.dump(Cat, file)


