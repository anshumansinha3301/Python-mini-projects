run_again = True 
# the outer while loop will keep running untill the run_again = False
while run_again:
    num1 = int(input("Enter first no: ")) #getting numbers from user
    num2 = int(input("Enter second no: "))

    try_again = True #while try_again is true inner loop will keep running
    while try_again:
        operator = input("Enter operation (+ - * /): ") #telling user what operation to perform
        print(" ") #line space for better UI
        
        #performing operation choosen by user
        if operator == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
            try_again = False #breaking the while loop after successfull operation
        elif operator == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
            try_again = False
        elif operator == "*":
            print(f"{num1} x {num2} = {num1 * num2}")
            try_again = False
        elif operator == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
            try_again = False
        else: #will run if none of the above operator is choosen
            print("Enter a valid operation") 
            # giving user another chance of choosing valid operation as try_again is still True

    print(" ")
    #telling user to continue or not
    choice = input("Do you want to calculate again Y/N: ").lower()
    if choice == "n":
        run_again = False #breaking the outer loop as per user's choice
        print("Good Bye!")
        print(" ")
    #the outer loop will run again if user's choice is 'y'