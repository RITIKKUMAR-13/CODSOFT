num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation: +, -, *, /")
choice = input("Enter choice: ")

if choice == '+':
    print("Result:", num1 + num2)
elif choice == '-':
    print("Result:", num1 - num2)
elif choice == '*':
    print("Result:", num1 * num2)
elif choice == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice")
