import os
import glob
import matplotlib.pyplot as plt
keywords = set()
keyword_count = dict()
#coun.key放區間 value放次數
coun = dict()
x=1995
y=3
z=0
x_axis=[]
y_axis=[]
file_paths = glob.glob(os.path.join("autonomous_vehicle_data_records", "*.txt"))
s="object detection"
# iterate through each file
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        # initialize keyword and insideDE
        keyword = ""
        insideDE = False
        # iterate through each line
        for line in file:
            # starts of keywords
            if line.startswith("DE "):
                insideDE = True
                keyword += line[3:].strip()
            # contents inside the DE tag
            elif line.startswith("   ") and insideDE:
                keyword += line[3:].strip()
            else:
                # add each keyword into the set and dictionary
                if keyword != "":
                    keyword = keyword.split(';')
                    for word in keyword:
                        word = word.strip().lower() # .lower() to avoid same keywords but with different upper/lower characters
                        if(word==s):
                            line = file.readline()
                            while line.startswith("PY ") != True:
                                line = file.readline()
                            if line.startswith("PY "):
                                    z+=1
                                    year=line[3:].strip()
                                    ke = int((int(line[3:].strip()) - x) / y)
                                    if ke in coun:
                                        coun[ke] += 1
                                    else:
                                        coun[ke] = 1                 
                # re-initialize keyword and insideDE
                keyword = ""
                insideDE = False
# sort the dictionary with it's value in descending order
while x<=2024:
    x_axis.append(x)
    x+=y
y_axis=[0] * len(x_axis)
for k, v in coun.items():
    y_axis[k]=v    
plt.bar(x_axis, y_axis)
plt.title(s)
plt.yticks(range(0, max(y_axis)+25, 25))
plt.show()
