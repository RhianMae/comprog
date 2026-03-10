answer = ""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Multiply")
print("2. Divide")
print("3. Add")
print("4. Subtract")

option = input("Choose operation: ")

if option == "1":
    print("Answer:", num1 * num2)
    answer = num1 * num2
    print("Answer:", int(answer))

elif option == "2":
    if num2 != 0:
        print("Answer:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")

elif option == "3":
    print("Answer:", num1 + num2)
    answer = num1 + num2
    print("Answer:", int(answer))

elif option == "4":
    print("Answer:", num1 - num2)
    answer = num1 - num2
    print("Answer:", int(answer))

else:
    print("Invalid input.")
    print("Please choose from the given options.")