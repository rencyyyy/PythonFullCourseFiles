# EXCEPTION - An event that interrupts the flow of a program
#             (ZeroDivisionError, Value Error, Type Error)
#             1. try, 2. except, 3. finally

#             VERY USEFUL TO DANGEROUS CODE THAT CAUSED AN ERROR

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:                       # When u attempt to divide a number to zero
    print("You cant divide by zero IDIOT!")
except ValueError:                              # Attempt to typecast a value of a wrong data type
    print("Invalid input, numbers only")
except Exception:                               # Broad unseen error
    print("Something went wrong and i don't know what it is")
finally:                                        # Always execute regardless there is an exception or not (Cleanup)
    print("Do some cleanup here")