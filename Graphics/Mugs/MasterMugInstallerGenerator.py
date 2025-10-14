import csv

TextParseDefsPath = "../../Text/ParseDefinitions.txt"
TextParseMarker = "[Marker_LoadMugsBelow] = [.]\n"
defsOutputPath="../../Definitions/Generated/MugIDs.event"

UseVanillaClassCardData = True

def intToHex(i):
    j = hex(i)
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)

mugsData = []
with open("Mugs.csv", mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        mugsData.append(lines)

mugsOutput = []
mugsDefsOutput = []
i = 2 # Because 0x1 is used up by the Capture skill

for mug in mugsData:
    name,mouthX,mouthY,eyeX,eyeY,palSwapOf,noMini = mug["Name"],mug["MouthX"],mug["MouthY"],mug["EyeX"],mug["EyeY"],mug["PalSwapOf"],mug["NoMini"]
    mugsDefsOutput.append(f"#define {name}_Mug "+intToHex(i)+"\n")

    if not palSwapOf: # Normal Processing
        mugsOutput.append(f"{name}_MugData:\n")
        mugsOutput.append(f"#incbin \"Dmp/{name}_mug.dmp\"\n")
        mugsOutput.append(f"{name}_MugFramesData:\n")
        mugsOutput.append(f"#incbin \"Dmp/{name}_frames.dmp\"\n")
        mugsOutput.append(f"{name}_MugPaletteData:\n")
        mugsOutput.append(f"#incbin \"Dmp/{name}_palette.dmp\"\n")
        if not noMini: # Yes Mini
            mugsOutput.append(f"{name}_MugMiniData:\n"),
            mugsOutput.append(f"#incbin \"Dmp/{name}_minimug.dmp\"\n"),
            mugsOutput.append(f"setMugEntryManual({name}_Mug, {name}_MugData, {name}_MugMiniData, {name}_MugPaletteData, {name}_MugFramesData, {mouthX},{mouthY},{eyeX},{eyeY})\n")
        else: # No Mini
            mugsOutput.append(f"setMugEntryManual({name}_Mug, {name}_MugData, 0x0, {name}_MugPaletteData, {name}_MugFramesData, {mouthX},{mouthY},{eyeX},{eyeY})\n")
    else: # Palette Swap
        mugsOutput.append(f"{name}_MugPaletteData:\n")
        mugsOutput.append(f"#incbin \"Dmp/{name}_palette.dmp\"\n")
        if not noMini: # Yes Mini
            mugsOutput.append(f"setMugEntryManual({name}_Mug, {palSwapOf}_MugData, {palSwapOf}_MugMiniData, {name}_MugPaletteData, {palSwapOf}_MugFramesData, {mouthX},{mouthY},{eyeX},{eyeY})\n")
        else: # No Mini
            mugsOutput.append(f"setMugEntryManual({name}_Mug, {palSwapOf}_MugData, 0x0, {name}_MugPaletteData, {palSwapOf}_MugFramesData, {mouthX},{mouthY},{eyeX},{eyeY})\n")
    i += 1
    mugsOutput.append("\n")
    print(f"Successfully processed mug {name}.")

with open("GeneratedMugsInstaller.event", "w") as w:
    w.writelines(mugsOutput)
print("Finished processing mugs.")

#Class Cards
print("Processing class cards.")
cardsData = []
carsdDefsOutput = []
with open("ClassCards.csv", mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        cardsData.append(lines)

cardsOutput = []
for card in cardsData:
    name = card["Name"]
    mugsDefsOutput.append("#define "+name+"_ClassCard"+" "+intToHex(i)+"\n")
    if UseVanillaClassCardData:
        cardsOutput.append("setCardEntry("+name+"_ClassCard, "+name+"_ClassCardData, "+name+"_ClassCardPaletteData)\n")
    else:
        cardsOutput.append(f"{name}_ClassCardData:\n")
        cardsOutput.append(f"#incbin \"DmpCards/{name}.dmp\"\n")
        cardsOutput.append(f"{name}_ClassCardPaletteData:\n")
        cardsOutput.append(f"#incbin \"DmpCards/{name}_pal.dmp\"\n")
        cardsOutput.append("setCardEntry("+name+"_ClassCard, "+name+"_ClassCardData, "+name+"_ClassCardPaletteData)\n")
    cardsOutput.append("\n")
    i += 1
    print("Successfully processed class card "+name+".")
    
with open("GeneratedCardsInstaller.event", "w") as writeCardInstaller:
    writeCardInstaller.writelines(cardsOutput)
print("Finished processing class cards.")

with open(defsOutputPath, "w") as w:
    w.writelines(mugsDefsOutput)
print("Wrote Mug definitions to "+defsOutputPath+".")

#LoadMugs for Text Parse Definitions 
parseDefsLoadMugs = []
names = []
for mug in mugsData:
    names.append(mug["Name"])
j = 1
#Generate the actual LoadMugs definitions
for name in names:
    parseDefsLoadMugs.append(f"[Load"+name+"] = [LoadPortrait]["+intToHex(j)+"][0x1]\n")
    j += 1
#Read current ParseDefs
with open(TextParseDefsPath, "r") as read:
    textParseData = read.readlines()
#Find index of the marker
for i in range(len(textParseData)):
    if textParseData[i] == TextParseMarker:
        markerIndex = i
        break
#Cut off everything after the marker (previous LoadMugs)
textParseData = textParseData[:markerIndex+1]
for loadMug in parseDefsLoadMugs:
    textParseData.append(loadMug)
#Write back to file
with open(TextParseDefsPath, "w") as write:
    write.writelines(textParseData)
print("Finished inserting new LoadMugs into ParseDefinitions.txt.")

input("Press enter to end program.")