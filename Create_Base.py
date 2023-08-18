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
def Creat_Cat(deck,stage):
    Base = list(combinations(deck,stage))
    Org_Base = []
    for i in Base:
        Org = sorted(i, key=lambda x: (x.number,x.suit),reverse=True)
        # S > H > D > C
        Org_Base.append(Org)
    Cat = []
    if stage == 2:
        for i in Org_Base:
            a = [i[0], i[1], -0.1, ""]
            Cat.append(a)
    elif stage == 3:
        for i in Org_Base:
            a = [i[0], i[1], i[2], -0.1, ""]
            Cat.append(a)
    else:
        for i in Org_Base:
            a = [i[0], -0.1, ""]
            Cat.append(a)
    return Cat

Cat = Creat_Cat(Deck,2)
Private_Data = os.path.join("D:\Texas hold em\Card_Base", "Private.pkl")
with open(Private_Data, 'wb') as file:
    pickle.dump(Cat, file)
for i in Cat:
    i[3] = str(i[0].suit) + str(i[0].number) + str(i[1].suit) + str(i[1].number)
    path = "D:\Texas hold em\Card_Base"
    path = os.path.join(path, i[3])
    os.mkdir(path)
    sub_dir = i[3]
    Flop_deck = Del_Card(sub_dir,Deck)
    Flop = Creat_Cat(Flop_deck,3)
    Flop_Data = os.path.join(path, "Flop.pkl")
    with open(Flop_Data, 'wb') as file:
        pickle.dump(Flop, file)
    for j in Flop:
        j[4] = str(j[0].suit) + str(j[0].number) + str(j[1].suit) + str(j[1].number) + str(j[2].suit) + str(j[2].number)
        Flop_path =os.path.join(path,j[4])
        os.mkdir(Flop_path)
        sub_dir = j[4]
        Turn_deck = Del_Card(sub_dir,Flop_deck)
        Turn = Creat_Cat(Turn_deck,1)
        Turn_Data = os.path.join(Flop_path, "Turn.pkl")
        with open(Turn_Data, 'wb') as file:
            pickle.dump(Turn, file)
        for k in Turn:
            k[2] = str(k[0].suit) + str(k[0].number)
            Turn_path = os.path.join(Flop_path, k[2])
            os.mkdir(Turn_path)
            sub_dir = k[2]
            River_deck = Del_Card(sub_dir, Turn_deck)
            River = Creat_Cat(River_deck, 1)
            River_Data = os.path.join(Turn_path, "River.pkl")
            with open(River_Data, 'wb') as file:
                pickle.dump(River, file)
            # for l in River:
            #     l[2] = str(l[0].suit) + str(l[0].number)
            #     River_path = os.path.join(Turn_path, l[2])
            #     os.mkdir(River_path)
            #     River_Data = os.path.join(River_path,"River.pkl")
            #     with open(River_Data, 'wb') as file:
            #         pickle.dump(River, file)


