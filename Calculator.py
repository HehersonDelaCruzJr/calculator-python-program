
while True:
    #Main Menu and The choices of Operations
    print("Welcome to Calculator!, Please Choose your Operation")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

    #The user will input their choice of operation
    operation = input("Enter your choice (Addition, Subtraction, Multiplication, Division): ")
    try:
        #Getting the data from user and ask the user if they want to try again with the operation
        if operation == 'Addition':
            while True:
                number1 = float(input("Please enter your first number: "))
                number2 = float(input("Please enter your second number: "))
                Answer = number1 + number2
                print("Result:", Answer)
                
                try_again = input("Do you want to try again? (Y/N): ")
                if try_again.upper() != 'Y' :
                    break

        elif operation == 'Subtraction':
            while True:
                number1 = float(input("Please enter your first number: "))
                number2 = float(input("Please enter your second number: "))
                Answer = number1 - number2
                print("Result:", Answer)

                try_again = input("Do you want to try again? (Y/N): ")
                if try_again.upper() != 'Y':
                    break

        elif operation == 'Multiplication':
            while True:
                number1 = float(input("Please enter your first number: "))
                number2 = float(input("Please enter your second number: "))
                Answer = number1 * number2
                print("Result:", Answer)

                try_again = input("Do you want to try again? (Y/N): ")
                if try_again.upper() != 'Y':
                    break

        #This lets the user know that in division the denominator can't be zero
        elif operation == 'Division':
            while True: 
                number1 = float(input("Please enter your first number: "))
                number2 = float(input("Please enter your second number: "))
                if number2 != 0:
                    Answer = number1 / number2
                    print("Result:", Answer)
                else:
                    raise ZeroDivisionError("Cannot divide by zero")
                
                try_again = input("Do you want to try again? (Y/N): ")
                if try_again.upper() != 'Y':
                        break
    
        else:
            print("Invalid input")
    except ValueError:
            print("Invalid Number Input")
    except ZeroDivisionError as e:
        print(str(e))
        
    #Ask the user if they want to continue if the user continue It will go back to selection of operation
    #if the user did not continue it will print "Thank you for using Calculator" and will exit
    try_again = input("Do you want continue? (Y/N): ")
    if try_again.upper() != 'Y':
        print("Thank you for using Calculator")
        break

