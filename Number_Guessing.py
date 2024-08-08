import random
 
def game(score):
    answer = random.randint(0, 5)
    try_left = 3
 
    while try_left > 0:
        print("=========================================")
        print("Try Left: " +  f"{try_left}")
        user_guess = input(f"{user_name}" + ", " + "Please Take your guess: ")
        print("=========================================")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please only enter a number")
            continue  # Ensure the loop doesn't proceed with invalid input
        try_left -= 1
        if user_guess == answer:
            score += 1  
            score_needed = 5 - score
            print("congratulations!!!")
            print("=====================")
            if score == 5:
                print("You Win!!!")
                print("ヾ(≧▽≦*)oヾ(≧▽≦*)oヾ(≧▽≦*)o")
                print("===================================")
                break
            else:
                print("You need " + f"{score_needed} more score to win")
            again(score)  # Pass the score to the again function
            return  # Exit the loop and function if the game continues
        else:
            print("You are so close, please try again.")
        if try_left == 0:
            print("======================================")
            print("Sorry " f"{user_name}, you have used all your tries")  
            print("======================================")
            again(score)  
            return  # Exit the loop and function if the game continues
 
def again(score):
    print("play again? Y or N")
    playagain = input(":")
    if playagain.lower() == "y":
        game(score)
    elif playagain.lower() == "n":
        print("Thank you for playing")
    else:
        print("Please only insert Y or N")
        again(score)
 
def to_start():
    print("======================================")
    start = input("Press 1 to start the Game: ")
    if start == "1":
        game(score)
    else:
        print("Please only insert 1")
        to_start()
 
score = 0
print("=========================")
print("  Number Guessing Game")
print("=========================")
user_name = input("Whats your name: ")
print("Hi, " + user_name + ", Welcome to the Number Guessing Game")
print("You will being asked to guess a number from 0 to 5.") 
print("You have 3 chances to guess the correct number.")  
to_start()
