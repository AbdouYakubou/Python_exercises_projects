import random

random_guess = random.randint(1, 10)

while True:
    user_guess = int(input("Guess a number: "))
    
    if user_guess > random_guess:
        print(" guess too high! Try again")
    elif user_guess < random_guess:
        print("guess too low! Try again")
    else:
        print("you guessedd correct!")
        break
    
    