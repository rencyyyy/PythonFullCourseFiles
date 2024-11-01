from script1 import *
def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script 2")
    favorite_drink("Coca-cola")
    favorite_food("Burger")
    print("Goodbye")

if __name__=='__main__':
    main()