# import os
# file_path = "TestDIR/FHTest.txt"
#
# if os.path.exists(file_path):
#     print(f"This file '{file_path}' exist")
# else:
#     print(f"The file '{file_path}' doesn't exist")

#-----------------------------------------------------------------------------------------------------------------------

# import os
# txt_data = "This is a new added text file"
# file_path = "TestDIR/writingFileTest.txt"
#
# try:
#     with open(file_path, "a")as file:
#         file.write("\n" + txt_data)
#         print(f" The file '{file_path}' was created")
# except FileExistsError:
#     print(f"The '{file_path}' is already exists!")
#-----------------------------------------------------------------------------------------------------------------------
# import os
# collections_data = ["row1","row2","row3","row4","row5"]
#
# file_path = "TestDIR/writingCollectionFileTest.txt"
# try:
#     with open(file_path, "w")as file:
#         for data in collections_data:
#             file.write(data + "\n")
#         print(f"The collection file '{file_path}' has been added")
# except Exception:
#     print("Something went wrong :(")
#-----------------------------------------------------------------------------------------------------------------------
# import os
# import json
#
# employees = {
#     'name': "Rency Delos Santos",
#     'age': 22,
#     'job': "Software Engineer",
# }
# file_path = "TestDIR/writingJsonFile.json"
#
# try:
#     with open(file_path, "w") as file:
#         json.dump(employees, file, indent=4)
#         print(f"The file '{file_path}' was created!")
# except Exception:
#     print("Something went wrong :(")

#-----------------------------------------------------------------------------------------------------------------------

import os
# import csv
#
# employees = [["name","age","job"],
#              ["Rency", 22, "Software Engineer"],
#              ["Jose",30, "Network Engineer"],
#              ["Pedro", 25, "Full Stacks Web Developer"]
#              ]
#
# file_path = "TestDIR/writingCsvFile.csv"
#
# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"The csv file '{file_path}' has been created")
# except Exception:
#     print("Something went wrong :(")

