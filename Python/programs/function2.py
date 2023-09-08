# keyword arguments

def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy")
    if (efficacy > 50) and (efficacy <= 75):
        print("seems not so effective, needs more trail")
    elif (efficacy > 75) and (efficacy < 90):
        print("can consider this vaccine")
    elif (efficacy >= 90):
        print("i can take a shot")
    else:
        print("needs more trails")

vac_feedback("prizer", 95)
print()
vac_feedback("co-vaccine", 78)
print()
vac_feedback("covax", 45)