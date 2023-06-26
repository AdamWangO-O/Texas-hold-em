from Organization import *
from Identification import *
from CardClass import *
import pickle
import pandas as pd

with open("Card_Base.pkl", 'rb') as file:
    Base = pickle.load(file)

Straight_flush = [] * 6
Four_kind = [] * 6
Full_house = [] * 6
Flush = [] * 6
Straight = [] * 6
Three_kind = [] * 6
Two_pairs = [] * 6
One_pair = [] * 6
High_card = [] * 6

count = 0
for i in Base:
    print (str(count) + " in " + str(len(Base)))
    count = count + 1
    if IdSF(i):
        Org = OrgSF(i)
        Org.insert(0,0)
        Straight_flush.append(Org)
    elif IdFK(i):
        Org = OrgFK(i)
        Org.insert(0, 0)
        Four_kind.append(Org)
    elif IdFH(i):
        Org = OrgFH(i)
        Org.insert(0, 0)
        Full_house.append(Org)
    elif IdFl(i):
        Org = OrgFl(i)
        Org.insert(0, 0)
        Flush.append(Org)
    elif IdSt(i):
        Org = OrgSt(i)
        Org.insert(0, 0)
        Straight.append(Org)
    elif IdTK(i):
        Org = OrgTK(i)
        Org.insert(0, 0)
        Three_kind.append(Org)
    elif IdTP(i):
        Org = OrgTP(i)
        Org.insert(0, 0)
        Two_pairs.append(Org)
    elif IdOP(i):
        Org = OrgOP(i)
        Org.insert(0, 0)
        One_pair.append(Org)
    else:
        Org = OrgHC(i)
        Org.insert(0, 0)
        High_card.append(Org)

with open("Straight_flush.pkl", 'wb') as file:
    pickle.dump(Straight_flush,file)
with open("Four_kind.pkl", 'wb') as file:
    pickle.dump(Four_kind,file)
with open("Full_house.pkl", 'wb') as file:
    pickle.dump(Flush,file)
with open("Flush.pkl", 'wb') as file:
    pickle.dump(Straight_flush,file)
with open("Straight.pkl", 'wb') as file:
    pickle.dump(Straight,file)
with open("Three_kind.pkl", 'wb') as file:
    pickle.dump(Three_kind,file)
with open("Two_pairs.pkl", 'wb') as file:
    pickle.dump(Two_pairs,file)
with open("One_pair.pkl", 'wb') as file:
    pickle.dump(One_pair,file)
with open("High_card.pkl", 'wb') as file:
    pickle.dump(High_card,file)
