#Calculator App

# Infinite loop to keep the calculator running until the user decides to exit
while True: 
    try: 
        # Prompt user to input two numbers
        num1 = int(input("Enter first no: ")) 
        num2 = int(input("Enter second no: "))
    except ValueError: 
        # If input is not a valid number, display error and restart loop
        print("Invalid input. Please enter numbers only.")
        print("") # Add a newline for better readability
        continue # Restart the outer loop

    # Inner loop to prompt for operator until a valid one is entered
    while True:
        
        operator = input("Enter operation (+ - * /): ") 
        print(" ") 
        
        # Addition
        if operator == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            break # Break the operator loop to return to outer loop
        
        # Subtraction
        elif operator == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            break

        # Multiplication
        elif operator == "*":
            result = num1 * num2
            print(f"{num1} x {num2} = {result}")
            break
        
        # Division
        elif operator == "/":
            if num2 != 0: # Prevent division by zero
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                break  
            else:
                print("Division by zero is not allowed")

        # Invalid operator input      
        else: 
            print("Enter a valid operation") 
            
    # Ask user if they want to perform another calculation
    print(" ")
    choice = input("Do you want to calculate again Y/N: ").lower()

    # Exit condition
    if choice == "n":
        print("Good Bye!")
        print(" ")
        break 