import datetime

# SET RANDOM DATE FORMAT | EDITED
my_birthdate = datetime.date(2002, 11, 20)
my_birthdate = my_birthdate.strftime("%m-%d-%Y")
print(f"My birthdate is '{my_birthdate}'")

# CHECK DATE TODAY
today = datetime.date.today()
print(f"Our date today is '{today}'")

# SET RANDOM TIME FORMAT
time = datetime.time(12,30,5)
print(f"Random time format '{time}'")

# CHECK DATE AND TIME TODAY & LIVE | EDITED
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S of %m-%d-%Y")
print(f"EDITED & LIVE DATE AND TIME TODAY IS '{now}'")

# CHECK OF THE DATE HAS PASSED OR NOT
target_datetime = datetime.datetime(2025,1,1, 12,00,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print(f"'{target_datetime}' has passed")
else:
    print(f"'{target_datetime}' has NOT passed")
