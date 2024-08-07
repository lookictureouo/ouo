def game():
    import random

    answer = random.randint(0,5)
    try_left = 3

    while try_left > 0:
        print("Try Left: " +  f"{try_left}")
        user_guess = input(f"{user_name}" + ", " + "Please Take your guess: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please only enter a number")
        try_left -= 1
        if user_guess == answer:
            try_left = 0
            print("congratulations!!!")
            again()
        else:
            print("You are so close, please try again.")
        
        if try_left == 0:
            print("Sorry " f"{user_name}, you have uses all your trys")
            again()




def again():
    print("play again? Y or N") 
    playagain = input(":" )
    if playagain.lower() == "y":
        game()
    elif playagain.lower() == "n":
        print("Thank u for playing")
    else: 
        print("Please only insert Y or N")
        return again()

def to_start():
    start = input("Press 1 to start the Game: ")
    try:
        print(start)
    except ValueError:
        print("Please only insert 1") #checking user only insert 1
    if start == "1":
        game()
    else:
        print("Please only insert 1")
        return to_start()


print("=========================")
print("  Number Guessing Game")
print("=========================")
user_name = input("Whats your name: ")
print("Hi, " + user_name + ", Welcome to the Number Guessing Game")
print("You will being asked to guess a number from 1 to 5.")
print("You have 3 chance to gets the correct number.")
to_start()

