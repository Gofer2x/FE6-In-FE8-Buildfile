import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def cullSupports(character):
    global pairs

    characterSupports = {}
    characterSupportsPartners = []

    # Set up dict of the character's supports and a list of their support partners.
    for pair in pairs:
        char1,char2 = pair[0],pair[1]
        if char1 == character:
            characterSupports[char2] = pair
            characterSupportsPartners.append(char2)
        elif char2 == character:
            characterSupports[char1] = pair
            characterSupportsPartners.append(char1)

    # Actually process the supports until there are few enough left.
    while len(characterSupportsPartners) > 7:
        print(f"Current {character} support count: "+str(len(characterSupportsPartners)))
        print(f"Please type in the name of a {character} partner to remove.")
        for partner in characterSupportsPartners:
            print(partner)
        toRemove = input("Partner to remove - ")
        try:
            characterSupportsPartners.remove(toRemove)
            pairs.remove(characterSupports[toRemove])
            characterSupports.pop(toRemove)
            print(f"Removed {toRemove}.")
        except Exception as e:
            print("Something went wrong.",e)
    return

# [char1,char2,initial,growth]
pairs = [
["Roy","Marcus",30,2], #ROY
["Roy","Alen",20,2], #ROY
["Roy","Lance",20,2], #ROY
["Roy","Wolt",30,2], #ROY
["Roy","Shanna",1,1], #ROY
["Roy","Sue",1,1], #ROY
["Roy","Lilina",56,4], #ROY, LILINA
["Roy","Larum",1,1], #ROY
["Roy","Cecilia",20,2], #ROY
["Roy","Sophia",1,1], #ROY
["Marcus","Alen",20,2],
["Marcus","Lance",20,2],
["Marcus","Wolt",20,2],
["Marcus","Lilina",1,1], #LILINA
["Alen","Lance",30,2],
["Alen","Wolt",20,2],
["Alen","Ward",1,1],
["Alen","Thea",1,1],
["Lance","Wolt",20,2],
["Lance","Lot",1,1],
["Lance","Clarine",1,1],
["Wolt","Sue",1,1],
["Bors","Astolfo",1,2],
["Bors","Lilina",30,2], #LILINA
["Bors","Barthe",20,2],
["Bors","Ogier",1,2],
["Bors","Gwendolyn",35,3],
["Elen","Chad",1,1],
["Elen","Lugh",30,1],
["Elen","Saul",1,1],
["Elen","Melady",20,2],
["Elen","Zeiss",10,2],
["Dieck","Ward",10,2],
["Dieck","Lot",10,2],
["Dieck","Shanna",10,2],
["Dieck","Clarine",1,1],
["Dieck","Rutger",10,1],
["Dieck","Klein",40,1],
["Ward","Lot",40,2],
["Ward","Shanna",10,2],
["Ward","Echidna",1,1],
["Lot","Shanna",10,2],
["Lot","Echidna",1,1],
["Shanna","Zelot",30,1],
["Shanna","Thea",30,3],
["Shanna","Juno",30,3],
["Chad","Lugh",30,2],
["Chad","Raigh",1,2],
["Chad","Cath",1,1],
["Chad","Hugh",1,1],
["Lugh","Raigh",20,3],
["Lugh","Melady",1,1],
["Lugh","Hugh",5,1],
["Clarine","Rutger",10,2],
["Clarine","Dorothy",1,1],
["Clarine","Klein",40,3],
["Rutger","Fir",1,1],
["Rutger","Dayan",1,1],
["Rutger","Karel",1,1],
["Saul","Dorothy",20,2],
["Saul","Cecilia",1,1],
["Saul","Igrene",1,1],
["Saul","Yoder",40,2],
["Dorothy","Sin",1,1],
["Dorothy","Perceval",1,1],
["Dorothy","Yoder",40,2],
["Sue","Sin",30,2],
["Sue","Fae",1,1],
["Sue","Dayan",40,3],
["Zelot","Trec",10,2],
["Zelot","Noah",10,2],
["Zelot","Thea",30,1],
["Zelot","Juno",40,3],
["Trec","Noah",10,2],
["Trec","Gonzalez",1,1],
["Trec","Melady",1,1],
["Trec","Juno",20,1],
["Noah","Fir",10,2],
["Noah","Juno",20,1],
["Noah","Karel",1,1],
["Astolfo","Lilina",30,2], #LILINA
["Astolfo","Barthe",1,2],
["Astolfo","Gwendolyn",1,2],
["Astolfo","Igrene",10,1],
["Lilina","Barthe",30,2],
["Lilina","Ogier",10,2], #LILINA
["Lilina","Gwendolyn",30,2], #LILINA
["Lilina","Gonzalez",30,2], #LILINA
["Lilina","Cecilia",50,1], #LILINA
["Lilina","Garrett",10,2], #LILINA
["Barthe","Ogier",10,2],
["Barthe","Gwendolyn",20,2],
["Ogier","Gwendolyn",10,2],
["Ogier","Larum",1,1],
["Fir","Sin",1,2],
["Fir","Bartre",40,3],
["Fir","Karel",30,3],
["Sin","Zeiss",1,1],
["Sin","Dayan",40,2],
["Geese","Larum",1,1],
["Geese","Echidna",1,1],
["Geese","Cath",20,1],
["Geese","Garrett",1,1],
["Geese","Douglas",1,1],
["Gonzalez","Echidna",1,1],
["Gonzalez","Bartre",1,1],
["Gonzalez","Garrett",20,1],
["Gonzalez","Dayan",1,1],
["Klein","Thea",30,2],
["Klein","Elffin",10,2],
["Klein","Perceval",20,2],
["Thea","Juno",30,3],
["Larum","Echidna",20,2],
["Larum","Perceval",1,2],
["Larum","Garrett",1,1],
["Larum","Douglas",30,3],
["Elffin","Perceval",20,2],
["Elffin","Cecilia",20,2],
["Elffin","Fae",1,1],
["Elffin","Douglas",30,2],
["Bartre","Cath",1,1],
["Bartre","Zeiss",1,1],
["Bartre","Karel",20,2],
["Raigh","Sophia",1,1],
["Raigh","Hugh",5,1],
["Raigh","Niime",1,1],
["Cath","Garrett",1,1],
["Cath","Hugh",1,1],
["Melady","Zeiss",20,3],
["Melady","Yoder",1,1],
["Perceval","Cecilia",30,2],
["Perceval","Douglas",30,2],
["Cecilia","Douglas",30,2],
["Sophia","Igrene",30,2],
["Sophia","Fae",30,3],
["Sophia","Niime",1,1],
["Igrene","Fae",30,3],
["Igrene","Douglas",1,1],
["Fae","Niime",1,1],
["Hugh","Niime",40,1],
["Zeiss","Karel",1,1],
["Niime","Yoder",40,1],
["Dayan","Yoder",1,1]]

charsInOrder = [
"Roy",
"Marcus",
"Alen",
"Lance",
"Wolt",
"Bors",
"Merlinus",
"Elen",
"Dieck",
"Ward",
"Lot",
"Shanna",
"Chad",
"Lugh",
"Clarine",
"Rutger",
"Saul",
"Dorothy",
"Sue",
"Zelot",
"Trec",
"Noah",
"Astolfo",
"Lilina",
"Barthe",
"Ogier",
"Gwendolyn",
"Fir",
"Sin",
"Geese",
"Gonzalez",
"Klein",
"Thea",
"Larum",
"Elffin",
"Echidna",
"Bartre",
"Raigh",
"Cath",
"Melady",
"Perceval",
"Cecilia",
"Sophia",
"Igrene",
"Garrett",
"Fae",
"Hugh",
"Zeiss",
"Douglas",
"Niime",
"Juno",
"Dayan",
"Yoder",
"Karel"]

template = {
    "Partner1ID": "BYTE 0\n",
    "Partner2ID": "BYTE 0\n",
    "Partner3ID": "BYTE 0\n",
    "Partner4ID": "BYTE 0\n",
    "Partner5ID": "BYTE 0\n",
    "Partner6ID": "BYTE 0\n",
    "Partner7ID": "BYTE 0\n",
    "Partner1InitValue": "BYTE 0\n",
    "Partner2InitValue": "BYTE 0\n",
    "Partner3InitValue": "BYTE 0\n",
    "Partner4InitValue": "BYTE 0\n",
    "Partner5InitValue": "BYTE 0\n",
    "Partner6InitValue": "BYTE 0\n",
    "Partner7InitValue": "BYTE 0\n",
    "Partner1Growth": "BYTE 0\n",
    "Partner2Growth": "BYTE 0\n",
    "Partner3Growth": "BYTE 0\n",
    "Partner4Growth": "BYTE 0\n",
    "Partner5Growth": "BYTE 0\n",
    "Partner6Growth": "BYTE 0\n",
    "Partner7Growth": "BYTE 0\n",
    "Amount": "BYTE 0\n",
    "Padding": "SHORT 0x0\n"
}

output = []

#This whole section is a bit of a mess but it works I guess.

roySupports = {}
lilinaSupports = {}
roySupportsPartners = []
lilinaSupportsPartners = []

for pair in pairs:
    char1,char2 = pair[0],pair[1]
    if char1 == "Roy":
        roySupports[char2] = pair
        roySupportsPartners.append(char2)
    elif char2 == "Roy":
        roySupports[char1] = pair
        roySupportsPartners.append(char1)

print("Both Roy and Lilina cannot have all of their FE6 supports, as the FE8 engine support cap is 7.\nYou will be asked which of their supports to remove to accommodate.")

cullSupports("Roy")
cullSupports("Lilina")

#Begin proper processing. Thresholds table.

for char in charsInOrder:
    output.append("ALIGN 4\n")
    output.append("//"+char+"\n")
    output.append(char+"SupportData:\n")
    pairsCurrent = []
    templateCurrent = template.copy()
    for pair in pairs:
        if char in pair:
            pairsCurrent.append(pair.copy())
    for i in range(len(pairsCurrent)):
        pairsCurrent[i].remove(char)
    if len(pairsCurrent) > 7:
        input(char+" has too many supports. Skipping. This will break things.")
    else:
        templateCurrent["Amount"] = ("BYTE "+ str(len(pairsCurrent))+" //Amount\n")
        for i in range(len(pairsCurrent)):
            pair = pairsCurrent[i]
            partner,init,growth = pair[0],str(pair[1]),str(pair[2])
            templateCurrent["Partner"+str(i+1)+"ID"] = "BYTE "+partner+" //Partner "+str(i+1)+"\n"
            templateCurrent["Partner"+str(i+1)+"InitValue"] = "BYTE "+init+" //Partner "+str(i+1)+" Intial Value\n"
            templateCurrent["Partner"+str(i+1)+"Growth"] = "BYTE "+growth+" //Partner "+str(i+1)+" Growth\n"
        for line in templateCurrent.values():
            output.append(line)
        output.append("\n")

with open("GeneratedSupportThresholdsTable.event","w") as w:
    w.writelines(output)


output = []

# Support convo table.

for pair in pairs:
    char1,char2 = pair[0],pair[1]
    output.append("//"+char1+" "+char2+"\n")
    output.append("SHORT "+char1+"\n")
    output.append("SHORT "+char2+"\n")
    output.append("SHORT "+char1+char2+"_SupportC\n")
    output.append("SHORT "+char1+char2+"_SupportB\n")
    output.append("SHORT "+char1+char2+"_SupportA\n")
    output.append("SHORT 0x0\n")
    output.append("SHORT 0x0\n")
    output.append("SHORT 0x0\n")

output.append("SHORT 0xFFFF 0x0 0x0 0x0 0x0 0x0 0x0 0x0 //Terminator\n")


with open("GeneratedSupportConvosTable.event","w") as w:
    w.writelines(output)

input("Done. Enter to exit.")