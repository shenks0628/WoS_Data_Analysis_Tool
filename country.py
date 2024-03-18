import os
import glob
import matplotlib.pyplot as plt
import re

countries = set()
country_count = dict()

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
                # re-initialize address and insidePA
                address = ""
                insidePA = False

# sort the dictionary with it's value in descending order
sorted_countries = sorted(country_count.items(), key=lambda x: x[1], reverse=True)

with open('output_country.txt', 'w') as file:
    for key, value in sorted_countries:
        print(f"{key}({value})", file=file)