import os
import glob

keywords = set()
keyword_count = dict()

file_paths = glob.glob(os.path.join("autonomous_vehicle_data_records", "*.txt"))

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
                        word = word.strip() # .lower() to avoid same keywords but with different upper/lower characters
                        keywords.add(word)
                        # if word in keyword_count, increase keyword_count[word] by one
                        # else, set keyword_count[word] to one
                        if keyword_count.get(word, False):
                            keyword_count[word] += 1
                        else:
                            keyword_count[word] = 1
                # re-initialize keyword and insideDE
                keyword = ""
                insideDE = False

# sort the dictionary with it's value in descending order
sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)

with open('output.txt', 'w') as file:
    for key, value in sorted_keywords:
        print(f"{key}({value})", file=file)