import matplotlib.pyplot as plt
from numpy import size
import pandas as pd
import random
import csv

#Defining varaities
V1 = ["FFbb", "Ffbb"] #Fast And Small
V2 = ["ffBB", "ffBb"] #Slow and Big



def Start():  # Function to summon initial members
    global Group1, Group2, Group3, Group4, members, G1_members, G2_members, G3_members, G4_members
    members = 0
    G1_members = G2_members = G3_members = G4_members = 0

    # Initialize groups as empty DataFrames
    Group1 = pd.DataFrame(columns=["Members", "GenoType", "PhenoType"])
    Group2 = pd.DataFrame(columns=["Members", "GenoType", "PhenoType"])
    Group3 = pd.DataFrame(columns=["Members", "GenoType", "PhenoType"])
    Group4 = pd.DataFrame(columns=["Members", "GenoType", "PhenoType"])

    # Add 2 starting members (Group1 and Group2 only)
    while members < 2:
        Group1.loc[G1_members] = [f"Member{G1_members+1}", str(random.choice(V1)), "Fast_And_Small"]
        Group2.loc[G2_members] = [f"Member{G2_members+1}", str(random.choice(V2)), "Slow_And_Big"]
        members += 1
        G1_members += 1
        G2_members += 1

    
def BreedRandom(PG1, PG2): #Function to breed random members of random groups
    global Group1, Group2, Group3, Group4, members, G1_members, G2_members, G3_members, G4_members
    P1 = random.choice(PG1["GenoType"])
    P2 = random.choice(PG2["GenoType"])

    s = [[P1[0]+P1[2], P1[0]+P1[3], P1[1]+P1[2], P1[1]+P1[3]],
         [P2[0]+P2[2], P2[0]+P2[3], P2[1]+P2[2], P2[1]+P2[3]]
        ]
    possibilities = [
                     [s[0][0] + s[1][0], s[0][0] + s[1][1], s[0][0] + s[1][2], s[0][0] + s[1][3]],
                     [s[0][1] + s[1][0], s[0][1] + s[1][1], s[0][1] + s[1][2], s[0][1] + s[1][3]],
                     [s[0][2] + s[1][0], s[0][2] + s[1][1], s[0][2] + s[1][2], s[0][2] + s[1][3]],
                     [s[0][3] + s[1][0], s[0][3] + s[1][1], s[0][3] + s[1][2], s[0][3] + s[1][3]]
                    ]
    offspring = random.choice(possibilities[random.randint(0, 3)])
    
    if "F" in offspring and "B" not in offspring:
        Group1.loc[G1_members] = [f"Member{G1_members+1}", str(offspring), "Fast_And_Small"]
        G1_members += 1
    elif "F" not in offspring and "B" in offspring:
        Group2.loc[G2_members] = [f"Member{G2_members+1}", str(offspring), "Slow_And_Big"]
        G2_members += 1
    elif "F" and "B" in offspring:
        Group3.loc[G3_members] = [f"Member{G3_members+1}", str(offspring), "Fast_And_Big"]
        G3_members += 1
    elif "F" and "B" not in offspring and "f" and "b" in offspring:
            Group4.loc[G4_members] = [f"Member{G4_members+1}", str(offspring), "Slow_AndSmall"]
            G4_members += 1
    

    members += 1

def Eating(GroupName, GroupNameP ,per1, per2, per3, VGroup1, VGroup2): #Function to manage eating 
    global ToBreedList, Food, FoodEaten, Group1, Group2, Group3, Group4, members, Deatlist
    FoodEaten = 0
    mems = 0
    for i in GroupName["GenoType"]:
        if Food > 0:
            eat = random.choices([0, 1, 2], [per1, per2, per3])[0]
            if eat == 0:
               GroupName = GroupName.drop(mems, axis=0)
               members -= 1
            if eat == 1:
                FoodEaten += 1
            if eat == 2:
                ToBreedList.append(i)
                FoodEaten += 2
            if GroupName is "Group2" or "Group3" and daysPassed > 0:
                chance = random.choices([0, 1], [3, 7])[0]
                if chance == 1:
                    VGroup1 = VGroup1.drop(mems, axis=0)
                    ToBreedList.append(i)

                chance2 = random.choices([0, 1], [5, 5])[0]
                if chance2 == 1:
                    VGroup2 = VGroup2.drop(mems, axis=0)
                    ToBreedList.append(i)
        mems += 1
        if Food <= 0:
            Deatlist.append(i)
    mems = 0


def Breed(): #Function to manage breeding between members who meet the requirments
    global ToBreedList, Group1, Group2, Group3, Group4, members, G1_members, G2_members, G3_members, G4_members
    for i in range(len(ToBreedList)//2):
        P1 = str(random.choice(ToBreedList))
        P2 = str(random.choice(ToBreedList))
        s = [
             [P1[0]+P1[2], P1[0]+P1[3], P1[1]+P1[2], P1[1]+P1[3]],
             [P2[0]+P2[2], P2[0]+P2[3], P2[1]+P2[2], P2[1]+P2[3]]
            ]
        possibilities = [
                     [s[0][0] + s[1][0], s[0][0] + s[1][1], s[0][0] + s[1][2], s[0][0] + s[1][3]],
                     [s[0][1] + s[1][0], s[0][1] + s[1][1], s[0][1] + s[1][2], s[0][1] + s[1][3]],
                     [s[0][2] + s[1][0], s[0][2] + s[1][1], s[0][2] + s[1][2], s[0][2] + s[1][3]],
                     [s[0][3] + s[1][0], s[0][3] + s[1][1], s[0][3] + s[1][2], s[0][3] + s[1][3]]
                    ]
        offspring = random.choice(possibilities[random.randint(0, 3)])
        if "F" in offspring and "B" not in offspring:
            Group1.loc[G1_members] = [f"Member{G1_members+1}", str(offspring), "Fast_And_Small"]
            G1_members += 1
        elif "F" not in offspring and "B" in offspring:
            Group2.loc[G2_members] = [f"Member{G2_members+1}", str(offspring), "Slow_And_Big"]
            G2_members += 1
        elif "F" and "B" in offspring:
            Group3.loc[G3_members] = [f"Member{G3_members+1}", str(offspring), "Fast_And_Big"]
            G3_members += 1
        elif "F" and "B" not in offspring:
            Group4.loc[G4_members] = [f"Member{G4_members+1}", str(offspring), "Slow_And_Small"]
            G4_members += 1
        members += 1

def Eat(): #Function to feed every group using Eating() Function
    global Food
    Eating(Group1, "Group1", 1, 6.5, 2.5, Group4, Group1)
    Food -= FoodEaten
    Eating(Group2, "Group2", 6.5, 2.5, 1, Group4, Group1)
    Food -= FoodEaten
    Eating(Group3, "Group3", 1, 6.5, 2.5, Group4, Group1)
    Food -= FoodEaten
    Eating(Group4, "Group4", 6.5, 2.5, 1, Group4, Group1)

def plot(): #Function to plot results
    plt.plot(x, G1D, label="Group1")
    plt.plot(x, G2D, label="Group2")
    plt.plot(x, G3D, label="Group3")
    plt.plot(x, G4D, label="Group4")
    
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.xlim([1, days])
    plt.ylim([1, days**2])
    plt.xticks(Xticks, label=[], size=5, rotation=45)
    plt.legend()
    plt.show()

def KWDE(): #Function to eliminate members who didn't get food
    global Deatlist, Group1, Group2, Group3, Group4
    for i in Deatlist:
         if "F" in i and "B" not in i:
             Group1 = Group1[Group1["GenoType"].str.contains(i) == False]
         elif "F" not in i and "B" in i:
             Group2 = Group2[Group2["GenoType"].str.contains(i) == False]
         elif "F" and "B" in i:
             Group3 = Group3[Group3["GenoType"].str.contains(i) == False]
         elif "F" and "B" not in i:
             Group4 = Group4[Group4["GenoType"].str.contains(i) == False]


days = int(input("Input Days: "))
daysPassed = 0
Food = int(input("Input Food count: "))
G1D, G2D, G3D, G4D = [], [], [], []
ToBreedList = []
Deatlist = []


Start()
for i in range(days):
    Eat()
    KWDE()
    print(Food)
    if len(ToBreedList) >= 2:
        Breed()
        ToBreedList = []
    BoN = random.choices([0, 1], [8, 2])[0]
    G1 = random.choice([Group1, Group2, Group3, Group4])
    G2 = random.choice([Group1, Group2, Group3, Group4])
    if BoN == 1:
        if len(G1.index) and len(G2.index) >= 2:
            BreedRandom(G1, G2)
    G1D.append(len(Group1.index))
    G2D.append(len(Group2.index))
    G3D.append(len(Group3.index))
    G4D.append(len(Group4.index))


print(Deatlist)
print(G1D, G2D, G3D, G4D)
x = []
Xticks = []
for i in range(days):
    x.append(int(i))
    Xticks.append(int(i))

plot()