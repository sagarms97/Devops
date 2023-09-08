# For loop
PLANET = "EARTH"

for i in PLANET :
    print(i)


vaccines = ("moderna", "pfizer", "sputnic", "covaxin")
for vac in vaccines :
    print(f"{vac} vaccine provides immunization against covid19" )


# While loop

x = 0
while x <= 10:
    print("value of x is", x)
    print("looping")
    x = x+1


########################################################
# Nested loop

vaccines = ("moderna", "pfizer", "sputnic", "covaxin")
for vac in vaccines :
    print("")
    print("I would like to a shot")
    for i in vac :
        print(i)









