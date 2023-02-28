# Getting the first number from the user
num_1_input = input("Enter the first number: ")
# Converting the first number from string to int
num_1 = int(num_1_input)
# Accepting the type of operation from the user
operation = input("Which Operation would you like to preform: ")
# Getting the second number from the user
num_2_input = input("Enter the second number: ")
# Converting the second number from string to int
num_2 = int(num_2_input)
# Calculating the result based on the operand (+, -, *, or /)
main = True

while main:
    if operation == "+":
        print("Your result is " + str((num_1 + num_2)))
        main = False
    elif operation == "-":
        print("Your result is " + str((num_1 - num_2)))
        main = False
    elif operation == "*":
        print("Your result is " + str((num_1 * num_2)))
        main = False
    elif operation == "/":
        print("Your result is " + str((num_1 / num_2)))
        main = False
    else:
        print("Not a valid operation")
        operation = input("Which Operation would you like to preform: ")
