import os
import glob
import pyrebase

TI = set()
cited_count = dict()

file_paths = glob.glob(os.path.join("autonomous_vehicle_data_records", "*.txt"))

# iterate through each file
for file_path in file_paths:
    #print(file_path.split('\\')[-1])
    with open(file_path, 'r', encoding="utf-8") as file:
        # initialize keyword and insideDE
        ti = ""
        pos = ""
        cnt = 0
        insideTI = False
        # iterate through each line
        for line in file:
            if line.startswith("TI "):
                insideTI = True
                ti += line[3:].strip()

            elif line.startswith("   ") and insideTI:
                ti += line[3:].strip()
            elif line.startswith("SO "):
                pos = file_path.split('\\')[-1]
                insideTI = False
            elif line.startswith("Z9 "):
                cnt = int(line[3:].strip())
                TI.add(ti)
                if ti != "":
                    if cited_count.get(ti, False):
                        cited_count[ti]["cited"] += cnt
                        cited_count[ti]["pos"] += f",{pos}"
                    else:
                        cited_count[ti] = dict()
                        cited_count[ti]["cited"] = cnt
                        cited_count[ti]["pos"] = pos

                ti = ""
                pos = ""
                cnt = 0
                insideTI = False

# sort the dictionary with it's value in descending order
sorted_TI = sorted(cited_count.items(), key=lambda x: x[1]["cited"], reverse=True)

with open('output_cited.txt', 'w') as file:
    for key, value in sorted_TI:
        print(f"{key}(Cited count:{value.get('cited')})(Position in {value.get('pos')})", file=file)