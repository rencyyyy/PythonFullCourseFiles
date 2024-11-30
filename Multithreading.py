# MULTITHREADING - Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from API's
#                  threading. Thread(Target=my_function)

import time
import threading

def pet_cat(first_name, last_name):
    time.sleep(6)
    print(f"You finish petting {first_name} {last_name}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# (SINGLE THREAD)
# PAG CINALL MO YUNG FUNCTION DITO. MAUUNANG I RUN YUNG WALK DOG AFTER 6 SECOND
# pet_cat()

# AND THEN MAG MOVE FORWARD SA SECOND FUNCTION NA TAKE TRASH, COUNT AGAIN FOR 2 SECOND BEFORE MAG DISPLAY YUNG FUNC
# take_out_trash()

# AND THEN ANOTHER NA NAMANG 4 SECOND BEFORE MAG DISPLAY YUNG SA GET MAIL
# get_mail()


# BUT USING MULTI THREADING SABAY SABAY SILANG MAG COCOUNT AT THE SAME TIME. THEN MAG DIDISPLAY SILA AFTER NUNG TIME NA
# NAKA INDICATE SA KANILA. (CONCURRENTLY)



chore1 = threading.Thread(target=pet_cat, args=("Buldak","Delos Santos"))               # (NOTE!) If may parameter sa function, wag kalimutan lagyan ng () yung argument because it's tuple.
chore1.start()                                                                          # Wag kalimutan lagyan ng "," yung value ng argument if isa lang siya, To let python know that This is a Tuple.

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# USE THIS JOIN METHOD PARA MA FINISH MUNA YUNG MGA CHORES OBJECT BEFORE MAG DISPLAY YUNG PRINT NA "All chores are finished!"
chore1.join()
chore2.join()
chore3.join()

print("All chores are finished!")