# import random
#
# #print("\u25cf \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# #          ●     ┌       ─      ┐      │      └      ┘
#
# # "┌─────────┐"
# # "│         │"
# # "│    ●    │"
# # "│         │"
# # "└─────────┘"
#
# dice_art = {
#     1: ("┌────────────┐",
#         "│            │",
#         "│      ●     │",
#         "│            │",
#         "└────────────┘"),
#     2: ("┌────────────┐",
#         "│  ●         │",
#         "│            │",
#         "│         ●  │",
#         "└────────────┘"),
#     3: ("┌────────────┐",
#         "│  ●         │",
#         "│      ●     │",
#         "│         ●  │",
#         "└────────────┘"),
#     4: ("┌────────────┐",
#         "│   ●    ●   │",
#         "│            │",
#         "│   ●    ●   │",
#         "└────────────┘"),
#     5: ("┌────────────┐",
#         "│  ●      ●  │",
#         "│      ●     │",
#         "│  ●      ●  │",
#         "└────────────┘"),
#     6: ("┌────────────┐",
#         "│  ●      ●  │",
#         "│  ●      ●  │",
#         "│  ●      ●  │",
#         "└────────────┘")
# }
#
# dice = []                                            # List of how many random dice selected (empty yet)
# total = 0                                            # (every die has number on it) The total sum of all dice "+"
# num_of_dice = int(input("Enter how many dice: "))    # The user will enter how many dice he wants to roll
#
# for die in range(num_of_dice):              # For every each die in range of the number of dice being rolled by user
#     dice.append(random.randint(1,6))  # Will add to the (empty) dice list, pero yung bawat dice na ni-rolled
#                                             # Eh may random numbers (argument) between 1 to 6.
#
# # HORIZONTAL - NOTE: Each tuple is made up of 5 elements.
# for line in range(5):                             # for every line in range of 5
#     for die in dice:                              # for each die in dice list
#         print(dice_art.get(die)[line], end="")    # get the die in dice aling the dictionary of dice art 1,6 line of 5
#     print()
#
#
# # VERTICAL
# # for die in range(num_of_dice):             # for every die in range of number of dice being rolled by user
# #     for line in dice_art.get(dice[die]):   # inner loop for every line in dice art dictionary get dice [die] counter
# #         print(line)
#
# for die in dice:                                 # Sa bawat die sa loob ng dice sa list
#     total += die                                 # ipag aadd yon para makuha yung total
# print(f"Total: {total}")                         # print yung total
