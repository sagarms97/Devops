# conditions and different data-types

devops = ["jenkins", "ansible", "bash-script", "python", "aws", "docker", "k8s"]
development = ("nodejs", "angular", "java", "asp.net", "python", "c++")
cntr_emp1 = {"name": "sagar", "skill": "blockchain", "code": 101}
cntr_emp2 = {"name": "rocky", "skill": "AI", "code": 102}

usr_skil = input("enter your desired skill:")
print(usr_skil)

# check in the database if we have this skill

if usr_skil in devops:
    print(f"we have {usr_skil} in devops")
elif usr_skil in development:
    print(f"we have {usr_skil} in development")
elif (usr_skil in cntr_emp1.values() or usr_skil in cntr_emp2.values()):
    print(f"we have {usr_skil} in contract employee")
else:
    print("we dont have such skill")
    print("check the value correct ")








