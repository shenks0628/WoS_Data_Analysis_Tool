import os
import glob
import pyrebase

TI = set()
reference_count = dict()

file_paths = glob.glob(os.path.join("autonomous_vehicle_data_records", "*.txt"))

# iterate through each file
for file_path in file_paths:
    #print(file_path.split('\\')[-1])
    with open(file_path, 'r', encoding="utf-8") as file:
        # initialize keyword and insideDE
        ti = ""
        author = []
        cnt = 0
        insideTI = False
        insideAF = False
        # iterate through each line
        for line in file:
            if line.startswith("AF "):
                insideAF = True
                author.append(line[3:].strip())
            elif line.startswith("   ") and insideAF:
                author.append(line[3:].strip())
            else :
                insideAF = False
            # starts of a title
            if line.startswith("TI "):
                insideTI = True
                ti += line[3:].strip()
            elif line.startswith("   ") and insideTI:
                ti += line[3:].strip()
            elif line.startswith("SO "):
                insideTI = False
            elif line.startswith("Z9 "):
                cnt = int(line[3:].strip())
                if ti != "":
                    if reference_count.get(ti, False):
                        reference_count[ti]["reference"] += cnt
                    else:
                        TI.add(ti)
                        reference_count[ti] = dict()
                        reference_count[ti]["reference"] = cnt
                        reference_count[ti]["author"] = author

                ti = ""
                author = []
                cnt = 0
                insideTI = False

# sort the dictionary with it's value in descending order
sorted_reference = sorted(reference_count.items(), key=lambda x: x[1]["reference"], reverse=True)

with open('output_reference.txt', 'w') as file:
    for key, value in sorted_reference:
        print(f"{key}(Reference count:{value.get('reference')})({value.get('author')})", file=file)