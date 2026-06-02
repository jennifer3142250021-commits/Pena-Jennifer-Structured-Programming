
def generate_email(name, lastname):
    return f"{name.lower()}.{lastname.lower()}@utd.edu.mx"

# Variable de control
continuar = "yes"

while continuar == "yes":
    name = input("Enter your name: ")
    lastname = input("Enter your lastname: ")

    generated_email = generate_email(name, lastname)

    print("Your institutional email is:", generated_email)

    continuar = input("Do you want to generate another email? (yes/no): ").lower()


#calculate_monthly_payment
total_payroll = 0

num_employees = int(input("How many employees does the company have? "))

for i in range(num_employees):
    print(f"\nEmployee #{i + 1}")

    name = input("Enter employee name: ")
    hours_worked = float(input("Enter hours worked this month: "))
    hourly_rate = float(input("Enter hourly pay rate: $"))

    monthly_pay = hours_worked * hourly_rate
    total_payroll += monthly_pay

    print(f"{name}'s monthly payment: ${monthly_pay:.2f}")

print(f"Total: ${total_payroll:.2f}")