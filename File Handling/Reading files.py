# Python reading files (.txt, .json, .csv)

# RELATIVE (Read content of a file) .txt

import os
#
file_path = "DirectoryTest/writingFiles.txt"
try:
    with open(file=file_path, mode="r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file doesn't exists!")
#-----------------------------------------------------------------------------------------------------------------------

# RELATIVE (Read content of a file) Collection.txt

file_path = "DirectoryTest/collectionWritingFiles.txt"

with open(file=file_path, mode="r") as file:
    content = file.read()
    print(content)

#-----------------------------------------------------------------------------------------------------------------------

# RELATIVE (Read content of a file) .json

# import os
import json

file_path = "DirectoryTest/jsonWritingFiles.json"
try:
    with open(file=file_path, mode="r") as file:
        content = json.load(file)
        print(content)

        # To Access content by it's key (Access specific value)
        print(content["name"])
        print(content["age"])
        print(content["position"])
except FileNotFoundError:
    print(f"The '{file_path}' was not found")

#-----------------------------------------------------------------------------------------------------------------------
import csv

file_path = "DirectoryTest/csvWritingFile.csv"
try:
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)                            # <--- delete if want to access specified column
            # To Access specific column
            # print(line[0])
            # print(line[1])                       # <--- Do not print examples (specific column) at the same time
            # print(line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read that file")

