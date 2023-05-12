#Main Menu and The choices of Operations
print("Welcome to Calculator!, Please Choose your Operation")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

#The user will input their choice of operation
operation = input(
    "Enter your choice (Addition, Subtraction, Multiplication, Division): ")

#Getting the data from user
if operation == 'Addition':
    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))
    Answer = number1 + number2
    print("Result:", Answer)

elif operation == 'Subtraction':
    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))
    Answer = number1 - number2
    print("Result:", Answer)

elif operation == 'Multiplication':
    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))
    Answer = number1 * number2
    print("Result:", Answer)
    

#This lets the user know that in division the denominator can't be zero
elif operation == 'Division':
    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))
    if number2 != 0:
        Answer = number1 / number2
        print("Result:", Answer)
    else:
        raise ZeroDivisionError("Cannot divide by zero")

