# Python File Detection

# import os                           # First you have to import os (Operating System)
#
# #   RELATIVE FILE (Within the same directory)
# file_path = "detectionTest.txt"     # If the file that you want to detect and current file is in the same directory <-
#
# if os.path.exists(file_path):
#     print(f"The file '{file_path}' exist!")
# else:
#     print("The file doesn't exist!")
#
# # RELATIVE FILE PATH (within/DIRECTORY)
#
# file_path2 = "DirectoryTest/detectionTest2.txt"
#
# if os.path.exists(file_path2):
#     print(f"The file '{file_path2}' in that directory exist!")
# else:
#     print(f"The file '{file_path2}' in that directory doesn't exist!")
#
# # ABSOLUTE FILE PATH (Different/FILE LOCATION)                              .txt, .pdf, .jpeg, .doc = extension
#
# absolute_file_path = "C:/Users/ASUS_LCL/Desktop/Rency/ciphertext.txt"       # Change  backward slash "\" into forward slash "/"
#                                                                             # Or double the backward slash "\\"
# if os.path.exists(absolute_file_path):
#     print(f"That location '{absolute_file_path}' file exist in your computer")
#
#     # inner if statement (Check if that file is directory or a file)        # (NOTE!: Don't forget to remove extension, to check if file or dir)
#     if os.path.isfile(absolute_file_path):                                  # Remove (/cipertext.txt) if you want to change output in condition
#         print("That is a file")                                             # because /Rency is a directory
#     elif os.path.isdir(absolute_file_path):
#         print("That is a directory")
# else:
#     print(f"That location '{absolute_file_path}' doesn't exist in your computer")