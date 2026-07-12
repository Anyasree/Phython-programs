def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

choice = input("Choose operation (+, -, *, /)")

if choice == "+":
    print(add(num1, num2))
elif choice == "-":
    print(subtract(num1, num2))
elif choice == "*":
    print(multiply(num1, num2))
elif choice == "/":
    print(divide(num1, num2))
else:
    print("Invalid operation")
    