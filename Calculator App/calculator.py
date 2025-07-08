import operator

# Mapping of symbols to actual functions
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# Infinite loop to keep the calculator running until the user decides to exit
while True: 
    try: 
        # Prompt user to input two numbers
        print(" ") # Add a newline for better readability
        num1 = int(input("Enter first no: ")) 
        num2 = int(input("Enter second no: "))
    except ValueError: 
        # If input is not a valid number, display error and restart loop
        print("Invalid input. Please enter numbers only.")
        continue # Restart the outer loop

    # Inner loop to prompt for operator until a valid one is entered
    while True:
        opr = input("Enter operation (+ - * /): ") 
        print(" ") 
        
        if num2 == 0 and opr == "/": # Prevent division by zero
            print("Division by zero is not allowed")
            continue # Restart the inner opr loop

        if opr in operations:    
            result = operations[opr](num1, num2)
            print(f"{num1} {opr} {num2} = {result}")
            break # Break the operator loop to return to outer loop
        else:
            print("Invalid operator. Try again.")
            print

    # Ask user if they want to perform another calculation
    print(" ")
    choice = input("Do you want to calculate again Y/N: ").lower()

    # Exit condition
    if choice == "n":
        print("Good Bye!")
        print(" ")
        break 