def menu():
    pass

def search():
    pass

def rent(movie_prize, user_order, movie_list):
    x = 1
    stock_UP = False
    user = False
    print()
    print()
    print("_________________________________________________")
    print()
    for i in movie_prize:
        print(x, end="")
        print(".", end=" ")
        print(i)
        x += 1
    print("_________________________________________________")
    print("Do you want to rent 0.rental_report 1.UP 2.The Hunger Game 3.Hachi: A Dog's Tale 4.Alex's Autobiography 5.FATE 6.Back to menu 7.Exit")
    user_input = int(input(": "))
    if user_input == 0:
        rental_report()
    elif user_input == 1:
        for cheking_stock in movie_list:
            if cheking_stock == "UP":
                stock_UP = True
            if stock_UP == True:
                pass
            else:
                while user != True:
                    print("UP is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                    user_input = input(": ")
                    if user_input >= 5 or user_input <= 0:
                        print("Please only insert 1, 2, 3, 4")
                    elif user_input == 1:
                        user = True
                    elif user_input == 2:
                        user = True
                    elif user_input == 3:
                        user = True
                    elif user_input == 4:
                        user = True
                    else:
                        print("Unknown Error Occur")
                

            

    


def returns():
    pass

def rental_report():
    pass

user_exit = False
user_order = []
movie_list = ["UP","The Hunger Game", "Hachi: A Dog's Tale","Alex's Autobiography", "FATE"]
movie_prize = ["UP                                    10$","The Hunger Game                       15$", "Hachi: A Dog's Tale                   30$","Alex's Autobiography                   1$", "FATE                                  20$"]
while user_exit != True:
    print("Welcome to Movie Rental System!")
    print("Please pick the opintion you trying to do")
    print("1.Rent 2.Return 3.Generate Rental Report 4.Exit \n")
    user_input = int(input("Your choice boss: \n"))
    if user_input == 1:
        rent(movie_prize, user_order, movie_list)
        user_exit = True


    if user_input == 4:
        user_exit = True
        print("Thanks for stopping by!\n")