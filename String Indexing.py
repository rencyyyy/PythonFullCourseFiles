# String Indexing - accessing elements of a sequence using [] (indexing operator)
#                   [start : end : step]

credit_card = "0912-45678-91235"

print(credit_card[1])     # Display second index of a var
print(credit_card[1:10])  # Start index 1 end index 10 (NOTE! end = exclusive)
print(credit_card[:10])   # Start index to index 10
print(credit_card[::2])   #STEP: 2 space ( 012,12,12,12)
print(credit_card[::-1])  # Display var as reverse (NOTE!: stepping index is negative)
print(credit_card[-1])    # Display the last index of a variable
last_digit = credit_card[-5:]
print(f"XXXX-XXXXX-{last_digit}")






