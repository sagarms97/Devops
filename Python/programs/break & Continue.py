import random

vaccines = ["moderna", "pfizer", "sputnic", "covaxin"]

random.shuffle(vaccines)
print(vaccines)

lucky = random.choice(vaccines)
print(lucky)

for vac in vaccines:
    print(f"testing vaccine {vac}")
    if vac == lucky:
        print("##################")
        print(f"{lucky} vaccine, test successfully")
        print()
        continue
        print("##################")
        print("test failed")
        print()
