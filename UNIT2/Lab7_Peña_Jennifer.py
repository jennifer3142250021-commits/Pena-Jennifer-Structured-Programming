def get_student_data():
    student = {}

    student["name"] = input("Enter your name: ")
    student["programming"] = int(input("Programming score (1-10): "))
    student["design"] = int(input("Design score (1-10): "))
    student["networking"] = int(input("Networking score (1-10): "))

    return student


def display_student(student):
    print("\nStudent Information:")
    
    for key, value in student.items():
        print(f"{key}: {value}")


def recommend_career(student):
    if student["programming"] > student["design"] and student["programming"] > student["networking"]:
        return "Software Developer"

    elif student["design"] > student["programming"] and student["design"] > student["networking"]:
        return "UI/UX Designer"

    else:
        return "Network Administrator"


def main():
    student = get_student_data()

    display_student(student)

    career = recommend_career(student)

    print("\nRecommended Career:", career)


main()
