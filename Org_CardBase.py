from Organization import *
from Identification import *
from CardClass import *
import pickle
import pandas as pd

with open("Card_Base.pkl", 'rb') as file:
    Base = pickle.load(file)

Straight_flush = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
Four_kind = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
Full_house = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
Flush = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
Straight = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
Three_kind = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
Two_pairs = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
One_pair = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])
High_card = pd.DataFrame(columns=['Index', 'Card1', 'Card2', 'Card3', 'Card4', 'Card5'])

for i in Base:
    if IdSF(i):
        Org = OrgSF(i)
        Straight_flush.loc[len(Straight_flush.index)] = [0, Org[0], Org[1],Org[2],Org[3],Org[4]]
    elif IdFK(i):
        Org = OrgFK(i)
        Four_kind.loc[len(Four_kind.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
    elif IdFH(i):
        Org = OrgFH(i)
        Full_house.loc[len(Full_house.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
    elif IdFl(i):
        Org = OrgFl(i)
        Flush.loc[len(Flush.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
    elif IdSt(i):
        Org = OrgSt(i)
        Straight.loc[len(Straight.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
    elif IdTK(i):
        Org = OrgTK(i)
        Three_kind.loc[len(Three_kind.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
    elif IdTP(i):
        Org = OrgTP(i)
        Two_pairs.loc[len(Two_pairs.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
    elif IdOP(i):
        Org = OrgOP(i)
        One_pair.loc[len(One_pair.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
    else:
        Org = OrgHC(i)
        High_card.loc[len(High_card.index)] = [0, Org[0], Org[1], Org[2], Org[3], Org[4]]
print (len(Base))
total = len(Straight_flush.index)+len(Four_kind.index)+len(Full_house.index)+len(Flush.index)+len(Straight.index)+len(Three_kind.index)+len(Two_pairs.index)+len(One_pair.index)+len(High_card.index)
print(total)