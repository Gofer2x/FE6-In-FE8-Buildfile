import csv

firstIndex = 2 #0x0 is blank, 0x1 is used up by the Capture skill.
TextParseDefsPath = "../../Text/ParseDefinitions.txt"
TextParseMarker = "[Marker_LoadMugsBelow] = [.]\n"
defsOutputPath="../../Definitions/Generated/MugIDs.event"

usedIDs = []
dataInstallerOutput = []
mugDefinitions = []
textParseLoadMugs = []

def intToHex(i):
    j = hex(int(i))
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)

def GetLowestUnusedIndex():
    i = firstIndex
    while (i in usedIDs) or (i in reservedIDs):
         i += 1
    return i

def PickAndCreateDataInstaller(data):
    if data["Type"] == "Mug":
        return CreateMugDataInstaller(data)
    elif data["Type"] == "Card":
        return CreateCardDataInstaller(data)

def CreateMugDataInstaller(mug):
    name,mouthX,mouthY,eyeX,eyeY,palSwapOf,noMini = mug["Name"],mug["MouthX"],mug["MouthY"],mug["EyeX"],mug["EyeY"],mug["PalSwapOf"],mug["NoMini"]
    output = []
    # Mug data
    if not palSwapOf:
        # Not palette swap, include new mug data
        mugDataReference = (f"{name}_MugData")
        output.append(f"{mugDataReference}:\n")
        output.append(f"#incbin \"Dmp/{name}_mug.dmp\"\n")
    else:
        # Palette swap, only use palette swap of value
        mugDataReference = (f"{palSwapOf}_MugData")
    
    # Frames data
    if not palSwapOf:
        # Not palette swap, include new mug frames data
        framesDataReference = (f"{name}_MugFramesData")
        output.append(f"{framesDataReference}:\n")
        output.append(f"#incbin \"Dmp/{name}_frames.dmp\"\n")
    else:
        # Palette swap, only use palette swap of value
        framesDataReference = (f"{palSwapOf}_MugFramesData")

    # Palette data, always the same
    paletteDataReference = (f"{name}_MugPaletteData")
    output.append(f"{paletteDataReference}:\n")
    output.append(f"#incbin \"Dmp/{name}_palette.dmp\"\n")

    # Mini mug data
    if not noMini:
        # Yes Mini
        if not palSwapOf:
            # Not palette swap, include new mini mug data
                miniMugReference = (f"{name}_MugMiniData")
                output.append(f"{miniMugReference}:\n")
                output.append(f"#incbin \"Dmp/{name}_minimug.dmp\"\n")
        else:
            # Palette swap, only use swap of value
                miniMugReference = (f"{palSwapOf}_MugMiniData")
    else:
        # No Mini
        miniMugReference = ("0x0")

    output.append(f"setMugEntryManual({name}_Mug, {mugDataReference}, {miniMugReference}, {paletteDataReference}, {framesDataReference}, {mouthX},{mouthY},{eyeX},{eyeY})\n")
    output.append("\n")
    print(f"Successfully processed mug {name}.")
    return output

def CreateCardDataInstaller(card):
    output = []
    name,useVanilla = card["Name"],card["CardUseVanillaData"]
    if useVanilla:
        output.append(f"setCardEntry({name}_ClassCard, {name}_ClassCardData, {name}_ClassCardPaletteData)\n")
    else:
        output.append(f"{name}_ClassCardData:\n")
        output.append(f"#incbin \"DmpCards/{name}.dmp\"\n")
        output.append(f"{name}_ClassCardPaletteData:\n")
        output.append(f"#incbin \"DmpCards/{name}_pal.dmp\"\n")
        output.append(f"setCardEntry({name}_ClassCard, {name}_ClassCardData, {name}_ClassCardPaletteData)\n")
    output.append("\n")
    print(f"Successfully processed card {name}.")
    return output

def CreateMugDefinitionAndParseDef(mug):
    global usedIDs
    name,reservedID = mug["Name"],mug["ReservedID"]
    if not reservedID:
        index = GetLowestUnusedIndex()
    else:
        reservedID = int(reservedID)
        index = reservedID
    definition = ("#define "+name+"_Mug "+intToHex(index)+"\n")
    parseDef = (f"[Load"+name+"] = [LoadPortrait]["+intToHex(index)+"][0x1]\n")
    usedIDs.append(index)
    print(definition.strip())
    print(parseDef.strip())
    return [definition,parseDef]
     
def CreateCardDefinition(card):
    global usedIDs
    name,reservedID = card["Name"],card["ReservedID"]
    if not reservedID:
        index = GetLowestUnusedIndex()
    else:
        reservedID = int(reservedID)
        index = reservedID
    definition = ("#define "+name+"_ClassCard "+intToHex(index)+"\n")
    usedIDs.append(index)
    print(definition.strip())
    return definition

mugsAndCardsData = []
with open("MugsAndCards.csv", mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        mugsAndCardsData.append(lines)

reservedIDs = []
for data in mugsAndCardsData:
    if data["ReservedID"]:
        reservedIDs.append(int(data["ReservedID"]))

for data in mugsAndCardsData:
    dataInstaller = PickAndCreateDataInstaller(data)
    if dataInstaller:
        for line in dataInstaller:
            dataInstallerOutput.append(line)
    if data["Type"] == "Mug":
        definition,parseDef = CreateMugDefinitionAndParseDef(data)
        mugDefinitions.append(definition)
        textParseLoadMugs.append(parseDef)
    if data["Type"] == "Card":
        definition = CreateCardDefinition(data)
        mugDefinitions.append(definition)
    
with open("GeneratedDataInstaller.event", "w") as w:
    w.writelines(dataInstallerOutput)

with open(defsOutputPath, "w") as w:
    w.writelines(mugDefinitions)


# Update ParseDefs
# Read current ParseDefs
with open(TextParseDefsPath, "r") as read:
    textParseData = read.readlines()
# Find index of the marker
for i in range(len(textParseData)):
    if textParseData[i] == TextParseMarker:
        markerIndex = i
        break
# Cut off everything after the marker (previous LoadMugs)
textParseData = textParseData[:markerIndex+1]
for loadMug in textParseLoadMugs:
    textParseData.append(loadMug)
# Write back to file
with open(TextParseDefsPath, "w") as write:
    write.writelines(textParseData)