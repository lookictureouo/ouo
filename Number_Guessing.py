def game():
    import random

    answer = random.randint(0,5)
    try_left = 3

    while try_left > 0:
        print("Try Left: " +  f"{try_left}")
        user_guess = input(f"{user_name}" + ", " + "Please Take your guess: ")
        try_left -= 1
        if user_guess == answer:
            pass
        else:
            pass



print("=========================")
print("  Number Guessing Game")
print("=========================")
user_name = input("Whats your name: ")
print("Hi, " + f"{user_name} ", + "Welcome to the Number Guessing Game")
print("You will being asked to guess a number from 1 to 5.")
print("You have 3 chance to gets the correct number.")
start = input("Press 1 to stat the Game: ")
try:
    print(start)
except ValueError:
    print("Please only insert 1") #checking user only insert 1
if start == 0:
    game()
else:
    print("Please only insert 1")

