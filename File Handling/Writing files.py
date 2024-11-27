# Python writing files (.txt, .json, .csv)
# Second parameter (MODE)  |  "w" = write, "x" = write (if file doesn't exist, elif does exist = ERROR!)
#                             "a" = append (to append a file), "r" = read

# RELATIVE
txt_data = "Hi, this is a text message"

file_path = "DirectoryTest/writingFiles.txt"
try:
    with open(file=file_path, mode="a") as file:          # if use "x" there's error (FileExistsError) now use exception
        file.write("\n" + txt_data)                              # delete that file first before running "x" to avoid error
        print(f"text file '{file_path}' was created")
except FileExistsError:
    print("That file is already exist!")


# if use "x" there's error (FileExistsError) now use exception
# delete that file first before running "x" to avoid error

#if use "a" u could add a new text data in that file ("\n" + ) before or after existing text for new line at - file.write method

#-----------------------------------------------------------------------------------------------------------------------

# # Create and writing collection within a file (RELATIVE)

collection_data = ["Web Developer", "Front-End Developer",
                   "Back-End Developer", "Software Engineer",
                   "Cyber Security", "Quality Ass."]

collection_file_path = "DirectoryTest/collectionWritingFiles.txt"
try:
    with open(collection_file_path, "w") as file:
        for data in collection_data:
            file.write(data + "\n")
except Exception:
    print("Something went wrong :(")


#-----------------------------------------------------------------------------------------------------------------------
# # Collection of key, value pairs
import json

employee = {
        'name': "rency",
        'age':  21,
        'position': "Software Engineer"
}
json_file_path = "DirectoryTest/jsonWritingFiles.json"
try:
    with open(json_file_path, "w") as file:                         # file add as the second argument (bcoz its json first)
        json.dump(employee, file, indent=4)                         # json.dump method will convert dictionary to a json string to output it keyword argument(indent = how many space)
        print(f"The json file '{json_file_path}' was created")      # just a confirmation message.
except Exception:
    print("Something went wrong :(")

#-----------------------------------------------------------------------------------------------------------------------
# CSV FILES (Comma seperated values) - Common in spreadsheet of data like an Excel spreadsheet

import csv

employees = [
            ["name","age","job"],               # Header row
            ["Rency",21,"Cyber Security"],      # data rows
            ["Juan",22,"Unemployed"],
            ["Pedro",20,"Priest"]
]

csv_file_path = "DirectoryTest/csvWritingFile.csv"
try:
    with open(csv_file_path, "w", newline="") as file:     # Keyword argument newline="" empty string (To avoid spaces)
        writer = csv.writer(file)                          # writer object created using csv.writer and pass the file
        for row in employees:
            writer.writerow(row)
        print(f"CSV file '{csv_file_path}' was created")
except Exception:
    print("Something went wrong :(")

# WRITEROW METHOD
# The writerow method is used in Python's csv module to write a single row of data into a CSV file.
#
# Key Points:
# Used With a CSV Writer Object: You first create a writer object using csv.writer() and then call writerow() on it.
# Accepts an Iterable: The method takes an iterable (like a list, tuple, or any object you can loop through) as its argument. Each item in the iterable represents a cell in the row.


