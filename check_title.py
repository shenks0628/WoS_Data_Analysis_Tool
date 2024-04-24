import os
import glob

count = 0
titles = set()
title_file = dict()
title_author = dict()

file_paths = glob.glob(os.path.join("autonomous_vehicle_data_records", "*.txt"))

# iterate through each file
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        # initialize author and insideAF
        author = []
        insideAF = False
        # initialize title and insideTI
        title = ""
        insideTI = False
        # iterate through each line
        for line in file:
            # starts of an author
            if line.startswith("AF "):
                insideAF = True
                author.append(line[3:].strip())
            # contents inside the AF tag
            elif line.startswith("   ") and insideAF:
                author.append(line[3:].strip())
            else:
                insideAF = False
            # starts of a title
            if line.startswith("TI "):
                insideTI = True
                title += line[3:].strip()
            # contents inside the TI tag
            elif line.startswith("   ") and insideTI:
                title += line[3:].strip()
            else:
                # print the current (title, file) and correspond (title, file) if the title has been seen before
                if title in titles:
                    print("---")
                    print(f'Title "{title}" appears in "{file_path}".')
                    print(f'Title "{title}" appears in "{title_file[title]}".')
                    # check if the authors are same
                    print(len(author))
                    for i in author:
                        print(i, end=" ")
                    print()
                    for i in title_author[title]:
                        print(i, end=" ")
                    print()
                    if len(set(author).intersection(title_author[title])) == len(author):
                        print(f'All Same!')
                    else:
                        print(f'Different!')
                    print("---")
                # add title count and add title, author into the set and dictionary
                if title != "" and len(author) != 0:
                    count += 1
                    titles.add(title)
                    title_file[title] = file_path
                    title_author[title] = author
                    # re-initialize author and insideAF
                    author = []
                    insideAF = False
                    # re-initialize title and insideTI
                    title = ""
                    insideTI = False

print(f"Number of titles: {count}")
print(f"Number of unique titles: {len(titles)}")