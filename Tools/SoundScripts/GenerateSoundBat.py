import csv, argparse

parser = argparse.ArgumentParser()
parser.add_argument('generatedSoundExchangeBatPath', type=str)
parser.add_argument('generatedEAFixBatPath', type=str)
parser.add_argument('csvPath', type=str)
parser.add_argument('febPath', type=str)
parser.add_argument('fromROMPath', type=str)
parser.add_argument('targetROMPath', type=str)
parser.add_argument('soundPrioFixEAPath', type=str)

args = parser.parse_args()

generatedSoundExchangeBatPath = args.generatedSoundExchangeBatPath
generatedEAFixBatPath = args.generatedEAFixBatPath
csvPath = args.csvPath
febPath = args.febPath
fromROMPath = args.fromROMPath
targetROMPath = args.targetROMPath
soundPrioFixEAPath = args.soundPrioFixEAPath

def intToHex(i):
    j = hex(i)
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)

def formatCmd(fromSongID, toSongID):
    return(f"%febPath% --rom=%targetROMPath% --songexchange --fromrom=%fromROMPath% --target=%targetROMPath% --fromsong={fromSongID} --tosong={toSongID}\n")

csvData = []
with open(csvPath, mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        csvData.append(lines)

fe6ID = None
fe8ID = None
cmdOutputExchange = []

eaFixOutput = [ "//Generated from CSV, Donut Touch\n",
                "#include \"../Definitions/Generated/NewFE6SoundIDs.event\" //This is being ran from inside EA's folder\n",
                "\n",
                "#define SoundTable 0x224470\n",
                "#define ChangeSoundTableEntryPriority(index,priority) \"PUSH ; ORG SoundTable+(8*index)+4 ; WORD priority ; POP\"\n",
                "\n",
                "#define Highest 0x0000000\n",
                "#define High 0x00010001\n",
                "#define MidHigh 0x00020002\n",
                "#define Medium1 0x00030003\n",
                "#define Medium2 0x00040004\n",
                "#define MidLow 0x00050005\n",
                "#define Low 0x00060006\n",
                "#define Lowest1 0x00070007\n",
                "#define Lowest2 0x00080008\n",
                "\n"]

for item in csvData:
    if item["Priority"]:
        name = item["Name"]
        priority = item["Priority"]
        eaFixOutput.append(f"ChangeSoundTableEntryPriority({name},{priority})\n")
with open(soundPrioFixEAPath,"w") as w:
    w.writelines(eaFixOutput)


cmdOutputExchange.append(f"set febPath={febPath}\n")
cmdOutputExchange.append(f"set fromROMPath={fromROMPath}\n")
cmdOutputExchange.append(f"set targetROMPath={targetROMPath}\n")
for item in csvData:
    #If the ID is "i", means iterative. Else, actual number.
    if item["FE6 ID"] == "i":
        fe6ID = int(fe6ID,16)
        fe6ID += 1
        fe6ID = intToHex(fe6ID)
    else:
        fe6ID = item["FE6 ID"]

    if item["FE8 Target ID"] == "i":
        fe8ID = int(fe8ID,16)
        fe8ID += 1
        fe8ID = intToHex(fe8ID)
    else:
        fe8ID = item["FE8 Target ID"]
    
    cmdOutputExchange.append(formatCmd(fe6ID,fe8ID))

with open(generatedSoundExchangeBatPath,"w") as w:
    w.writelines(cmdOutputExchange)

# Move to EA folder and run the priority fix EA.
cmdOutputFix = f"""set soundPrioFixEAPath={soundPrioFixEAPath}
set targetROMPath={targetROMPath}
cd %~dp0EventAssembler
ColorzCore A FE8 -output:%~dp0%targetROMPath% -input:%~dp0%soundPrioFixEAPath% --build-times
cd %~dp0"""

with open(generatedEAFixBatPath,"w") as w:
    w.write(cmdOutputFix)