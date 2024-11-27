import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

# print(f"CHARACTERS: {chars}")
# print(f"KEYS: {keys}")

# ENCRYPTION
print("-----------------------------------------------------------")
print("               MESSAGE ENCRYPTION PROGRAM                  ")
print("-----------------------------------------------------------")
plain_text = input("Enter message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"ORIGINAL MESSAGE: {plain_text}")
print(f"ENCRYPTED MESSAGE: {cipher_text}")

print()
# DECRYPTION
cipher_text = input("Enter message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"CIPHERTEXT MESSAGE: {cipher_text}")
print(f"DECRYPTED MESSAGE: {plain_text}")
