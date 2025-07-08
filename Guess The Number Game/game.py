import random

num = random.randint(1, 51) #generates random number b/w 1 & 50 (1 & 50 included)
attempts_left = 10 #user has 10 attempts to guess the right number

while True: 
    print(f"Attempts left = {attempts_left}") #will show how many attempts are left
    guess = int(input("Guess the number between 1 to 50: ")) #user has to guess the number b/w the given range

    #will check if the number matches the guess or not
    if guess > num:
        print("Too High")
        attempts_left -= 1 #will decrement the number of attempts by 1 after each loss 
    elif guess < num:
        print("Too Low")
        attempts_left -= 1
    else:
        print("You won 🎉") #if guess = number 
        break #will stop the while loop to end the game
    
    if attempts_left == 0: #will check if no attempts are left
        print("You lost 🥲") #if yes user will lost the game
        break