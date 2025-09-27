import argparse, csv, os, re, time

parser = argparse.ArgumentParser(description='Reads Nightmare .csv tables to automatically create EventAssembler ID definitions using Enumerate. Names are taken from the leftmost field.')
parser.add_argument('input', type=str, help='Path of the input .csv to process.')
parser.add_argument('output', type=str, help='Path of the final output .event file with IDs.')
parser.add_argument('enumeratePath', type=str, help='Path to the tool Enumerate.py.')
parser.add_argument('valueType', type=str, help='Name of the type of object being ID\'d. Used for blank items.')
parser.add_argument('--ignoreFirstItem', action='store_true', help='Ignores the first item in the .csv table.')
parser.add_argument('--oneIndexed', action='store_true', help='Starts the IDs at 1 instead of 0.')
args = parser.parse_args()

input = args.input
output = args.output
enumeratePath = args.enumeratePath
valueType = args.valueType
ignoreFirstItem = args.ignoreFirstItem
oneIndexed = args.oneIndexed

# Filename without extension.
filename = os.path.split(input)[1].replace(".csv","")

# Read .csv data.
fields = []
rows = []
with open(input, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

values = []
# Take leftmost row's value and use it as a name.
for row in rows:
    value = row[0]
    value = re.sub(r'\W+','', value )
    values.append(value)

blankCounter = 1

# Cut off first item.
if ignoreFirstItem:
    values = values[1:]

# First value as 1 or 0.
if oneIndexed:
    values[0] = values[0]+" 1"
else:
    values[0] = values[0]+" 0"
for i in range(len(values)):
    
    # Replace the empty values with "BlankVALUE".
    if values[i] == "":
        values[i] = "Blank"+valueType+str(blankCounter)
        blankCounter += 1
    values[i] = values[i]+"\n"

# Temporary file to use with Enumerator.
tempFilePath = "Temp"+filename+".txt"

print(f"Writing {tempFilePath}")
with open(tempFilePath,'w') as write:
    write.writelines(values)

print(f"Running Enumerator on {tempFilePath}")
os.system('%s %s %s' % (enumeratePath, tempFilePath, output))
os.remove(tempFilePath)

print("Exiting.")
#time.sleep(1)