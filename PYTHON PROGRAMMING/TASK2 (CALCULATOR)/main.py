# This will be a very basic consol based program to use the calculator

print("Welcome to the Pylator(A Python Calculator 😁)\n\n")
num1 = float(input("Please enter the first number: "))

operator = input(
    "\n\nPlease select one any one operator\n1. For addition: +\n2. For subtraction: -\n3. For multiplication: *\n4. For division: /\n5. For modular operations: %\n"

)

num2 = float(input("\nPlease Select the second number:) "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2

print(f"\n\n{num1} {operator} {num2} = {result}")