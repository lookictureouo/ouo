import random
 
def game(score):
    answer = random.randint(0, 5)
    try_left = 3
    print("-----------------------------------------") # For Nice looking Exterior 

    while try_left > 0: # Checking if the user have try left to keep playiny the round
        
        print("Try Left: " +  f"{try_left}")
        user_guess = input(f"{user_name}" + ", " + "Please Take your guess: ")
        print("-----------------------------------------") # For Nice looking Exterior 
        try: 
            user_guess = int(user_guess)
        except ValueError:
            print("Please only enter a number") # Cheaking did user put int 
            print("---------------------------") # For Nice looking Exterior 
            continue  # Ensure the loop doesn't proceed with invalid input
        try_left -= 1
        if user_guess == answer:
            score += 1  
            score_needed = 5 - score
            print("congratulations!!!")
            print("=====================") # For Nice looking Exterior
            if score == 5:
                print("You Win!!!")
                print("ヾ(≧▽≦*)oヾ(≧▽≦*)oヾ(≧▽≦*)o")
                print("===================================") # For Nice looking Exterior
                break # To force end the program
            else:
                print("You need " + f"{score_needed} more score to win") # Telling user how many more they need to win 
            again(score)  # Pass the score to the again function
            return  # Exit the loop and function if the game continues
        else:
            print("You are so close, please try again.")

        if try_left == 0: # Checking if user is out of trys
            print("======================================") # For Nice looking Exterior
            print("Sorry " f"{user_name}, you have used all your tries")  
            print("======================================") # For Nice looking Exterior
            again(score)  
            return  # Exit the loop and function if the game continues

        """
        This is the whole gaming fuction. 
        User guess the number in this function
        """
 
def again(score):
    print("play again? Y or N")
    playagain = input(":")
    if playagain.lower() == "y":
        game(score)
    elif playagain.lower() == "n":
        print("Thank you for playing")
    else:
        print("==========================") # For Nice looking Exterior
        print("Please only insert Y or N")
        print("==========================") # For Nice looking Exterior
        again(score)

    """
    This is for checking if the user want to play again.

    """
 
def to_start():
    print("======================================") # For Nice looking Exterior
    start = input("Press 1 to start the Game: ")
    if start == "1":
        game(score)
    else:
        print("======================================") # For Nice looking Exterior
        print(" Please only insert 1")
        to_start()
    """
    This checking if user want to start the game
    """


score = 0
print("=========================") # For Nice looking Exterior
print("  Number Guessing Game")
print("=========================") # For Nice looking Exterior
user_name = input("Whats your name: ")
print("Hi, " + user_name + ", Welcome to the Number Guessing Game")
print("You will being asked to guess a number from 0 to 5.") 
print("You have 3 chances to guess the correct number.")  
to_start()
