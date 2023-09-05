import calendar
import datetime
import os

year = 2023
month = 9
day = datetime.date.today()
x = calendar.month(year, month)
print(x)
print(day)

######################################################

n = int(input("Enter a number :"))
for i in range(1, 11):
    result = n * i
    print(f"{n} * {i} = {result}")

#############################################
userlist = ["alpha", "gamma", "beta"]

print("adding users.........")
for user in userlist:
    exitcode = os.system(f"id {user}")
    if exitcode != 0:
        print(f"id {user} doesn't exist, so adding it")
        os.system(f"useradd {user}")
        print()
    else:
        print(f"id {user} already exist")
        print()

