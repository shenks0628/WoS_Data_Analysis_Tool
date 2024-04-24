import os
import glob
import matplotlib.pyplot as plt
import re

target_country = "SWITZERLAND" # fill in the country name you want to look for
countries = set()
country_count = dict()

year = 1995
diff = 1
x_axis = []
y_axis = []
year_count = dict()

file_paths = glob.glob(os.path.join("autonomous_vehicle_data_records", "*.txt"))

# iterate through each file
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        # initialize address and insidePA
        address = ""
        insidePA = False
        # iterate through each line
        for line in file:
            # starts of address
            if line.startswith("PA "):
                insidePA = True
                address += line[3:].strip()
            # contents inside the PA tag
            elif line.startswith("   ") and insidePA:
                address += line[3:].strip()
            else:
                # pick out the country name and add it into the set and dictionary
                # but not every data has the same format, so some country cannot be captured by the following code
                if address != "":
                    # get the country name from address (usually the last word) and remove the non-alphabets
                    country = re.sub(r'[^a-zA-Z]', '', address.split(' ')[-1])
                    countries.add(country)
                    if country_count.get(country, False):
                        country_count[country] += 1
                    else:
                        country_count[country] = 1
                    if country == target_country:
                        line = file.readline()
                        while line.startswith("PY ") != True:
                            line = file.readline()
                        if line.startswith("PY "):
                                t = int((int(line[3:].strip()) - year) / diff)
                                if t in year_count:
                                    year_count[t] += 1
                                else:
                                    year_count[t] = 1
                # re-initialize address and insidePA
                address = ""
                insidePA = False

while year <= 2024:  # 將年份區間資料丟入list
    x_axis.append(year)
    year += diff
y_axis = [0] * len(x_axis) # 產生一個跟年份資料一樣大的list來裝出現次數
for k, v in year_count.items():  # 出現次數
    y_axis[k] = v
plt.bar(x_axis, y_axis) # 產生圖表 x軸是年分  y軸是次數
plt.title(target_country)
plt.yticks(range(0, max(y_axis)+500, 500))
plt.show()
