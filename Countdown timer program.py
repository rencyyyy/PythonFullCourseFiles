import time

# Seconds i % 60
# Minutes int(i /60) % 60
# Hours = int(i / 300)

my_Time = int(input("Enter your time in seconds: "))

for i in range(my_Time, 0, -1):
    seconds = i % 60
    minutes = int (i / 60 ) % 60
    hours = int ( i / 3600) % 24
    days = int (i / 86400) % 31
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIMES UP!")

