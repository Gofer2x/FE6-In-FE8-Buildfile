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

cmdOutputExchange.append(f"set febPath={febPath}\n")
cmdOutputExchange.append(f"set fromROMPath={fromROMPath}\n")
cmdOutputExchange.append(f"set targetROMPath={targetROMPath}\n")
for item in csvData:
    name = item["Name"]

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


cmdOutputFix = [] #ea fix
cmdOutputFix.append(f"set soundPrioFixEAPath={soundPrioFixEAPath}\n")
cmdOutputFix.append(f"set targetROMPath={targetROMPath}\n")
# Move to EA folder and run the priority fix EA.
cmdOutputFix.append("cd %~dp0EventAssembler\n")
cmdOutputFix.append(f"ColorzCore A FE8 -output:%~dp0%targetROMPath% -input:%~dp0%soundPrioFixEAPath% --build-times\n")
cmdOutputFix.append("cd %~dp0")

with open(generatedEAFixBatPath,"w") as w:
    w.writelines(cmdOutputFix)