import pickle

with open("Straight_flush.pkl", 'rb') as file:
    Straight_flush = pickle.load(file)
with open("Four_kind.pkl", 'rb') as file:
    Four_kind = pickle.load(file)
with open("Full_house.pkl", 'rb') as file:
    Full_house = pickle.load(file)
with open("Flush.pkl", 'rb') as file:
    Flush = pickle.load(file)
with open("Straight.pkl", 'rb') as file:
    Straight = pickle.load(file)
with open("Three_kind.pkl", 'rb') as file:
    Three_kind = pickle.load(file)
with open("Two_pairs.pkl", 'rb') as file:
    Two_pairs = pickle.load(file)
with open("One_pair.pkl", 'rb') as file:
    One_pair = pickle.load(file)
with open("High_card.pkl", 'rb') as file:
   High_card = pickle.load(file)

Straight_flush = sorted(Straight_flush, key=lambda x: (x[1].number),reverse=True)
for i in range (1,len(Straight_flush)):
    if Straight_flush[i][1].number != Straight_flush[i-1][1].number:
        Straight_flush[i][0] = Straight_flush[i-1][0] + 1
    else:
        Straight_flush[i][0] = Straight_flush[i-1][0]

Four_kind = sorted(Four_kind, key=lambda x: (x[1].number,x[5].number),reverse=True)
for i in range (1,len(Four_kind)):
    Flag = True
    for j in range (1,6):
        if Four_kind[i][j].number != Four_kind[i-1][j].number:
            Flag = False
            break
    if Flag == True:
        Four_kind[i][0] = Four_kind[i - 1][0]
    else:
        Four_kind[i][0] = Four_kind[i - 1][0] + 1

Full_house = sorted(Full_house, key=lambda x: (x[1].number,x[4].number),reverse=True)
for i in range (1,len(Full_house)):
    Flag = True
    for j in range (1,6):
        if Full_house[i][j].number != Full_house[i-1][j].number:
            Flag = False
            break
    if Flag == True:
        Full_house[i][0] = Full_house[i - 1][0]
    else:
        Full_house[i][0] = Full_house[i - 1][0] + 1

Flush = sorted(Flush, key=lambda x: (x[1].number,x[2].number,x[3].number,x[4].number,x[5].number),reverse=True)
for i in range (1,len(Flush)):
    Flag = True
    for j in range (1,6):
        if Flush[i][j].number != Flush[i-1][j].number:
            Flag = False
            break
    if Flag == True:
        Flush[i][0] = Flush[i - 1][0]
    else:
        Flush[i][0] = Flush[i - 1][0] + 1

Straight = sorted(Straight, key=lambda x: (x[1].number),reverse=True)
for i in range (1,len(Straight)):
    if Straight[i][1].number != Straight[i-1][1].number:
        Straight[i][0] = Straight[i-1][0] + 1
    else:
        Straight[i][0] = Straight[i-1][0]

Three_kind = sorted(Three_kind, key=lambda x: (x[1].number,x[4].number,x[5].number),reverse=True)
for i in range (1,len(Three_kind)):
    Flag = True
    for j in range (1,6):
        if Three_kind[i][j].number != Three_kind[i-1][j].number:
            Flag = False
            break
    if Flag == True:
        Three_kind[i][0] = Three_kind[i - 1][0]
    else:
        Three_kind[i][0] = Three_kind[i - 1][0] + 1

Two_pairs = sorted(Two_pairs, key=lambda x: (x[1].number,x[3].number,x[5].number),reverse=True)
for i in range (1,len(Two_pairs)):
    Flag = True
    for j in range (1,6):
        if Two_pairs[i][j].number != Two_pairs[i-1][j].number:
            Flag = False
            break
    if Flag == True:
        Two_pairs[i][0] = Two_pairs[i - 1][0]
    else:
        Two_pairs[i][0] = Two_pairs[i - 1][0] + 1

One_pair = sorted(One_pair, key=lambda x: (x[1].number,x[3].number,x[4].number,x[5].number),reverse=True)
for i in range (1,len(One_pair)):
    Flag = True
    for j in range (1,6):
        if One_pair[i][j].number != One_pair[i-1][j].number:
            Flag = False
            break
    if Flag == True:
        One_pair[i][0] = One_pair[i - 1][0]
    else:
        One_pair[i][0] = One_pair[i - 1][0] + 1

High_card = sorted(High_card, key=lambda x: (x[1].number,x[2].number,x[3].number,x[4].number,x[5].number),reverse=True)
for i in range (1,len(High_card)):
    Flag = True
    for j in range (1,6):
        if High_card[i][j].number != High_card[i-1][j].number:
            Flag = False
            break
    if Flag == True:
        High_card[i][0] = High_card[i - 1][0]
    else:
        High_card[i][0] = High_card[i - 1][0] + 1

with open("Straight_flush.pkl", 'wb') as file:
    pickle.dump(Straight_flush,file)
with open("Four_kind.pkl", 'wb') as file:
    pickle.dump(Four_kind,file)
with open("Full_house.pkl", 'wb') as file:
    pickle.dump(Full_house,file)
with open("Flush.pkl", 'wb') as file:
    pickle.dump(Flush,file)
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
