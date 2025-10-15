import csv, argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputCsvPath', type=str, help='Path of the input .csv to process.')
parser.add_argument('outputIDsPath', type=str, help='Path of the final output .event file with IDs.')
args = parser.parse_args()

inputCsvPath = args.inputCsvPath
outputIDsPath = args.outputIDsPath

csvData = []
with open(inputCsvPath, mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        csvData.append(lines)

output = []

id = None

for item in csvData:
    name = item["Name"]

    if item["FE8 Target ID"] == "i":
        id = hex(int(id,16)+1).upper().replace("X","x")
    else:
        id = item["FE8 Target ID"]    

    define = (f"#define {name} {id}\n")
    print(define,end="")
    output.append(define)

with open(outputIDsPath,"w") as write:
    write.writelines(output)

print("Done updating sound IDs.")