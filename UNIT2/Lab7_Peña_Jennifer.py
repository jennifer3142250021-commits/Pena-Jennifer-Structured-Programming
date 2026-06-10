student={}
student["name"]=input("Enter yur name:")
student["programming"]=int(input("programming score (1-10):"))
student["design"]=int(input("design score (1-10):"))
student["networking"]=int(input("networking score(1-10):"))

for key, value in student.items():
    print(f"{key}:{value}")

if student["programming"] > student["design"] and student["programming"] > student["networking"]:

    career = "Software Developer"

elif student["design"] > student["programming"] and student["design"] > student["networking"]:

    career = "UI/UX Designer"

else:

    career = "Network Administrator"


print("Recommended Career:", career)