def menu():
    pass

def search():
    pass

def rent(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE):
    x = 1
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
    return rent2(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE)

def rent2(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE):
    finish_renting = False
    user = False
    print("Do you want to rent 0.rental_report 1.UP 2.The Hunger Game 3.Hachi: A Dog's Tale 4.Alex's Autobiography 5.FATE 6.Back to menu 7.Exit")
    user_input = int(input(": "))
    try:
        print(user_input)
    except ValueError:
        print("Please only insert 1, 2, 3, 4")
    if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 5 and user_input != 6 and user_input != 7:
        print("Please only insert 1, 2, 3, 4")
        return rent2(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE)
    else:
        while finish_renting !=  True:
            if user_input == 0:
                rental_report()
            elif user_input == 1:
                if cheking_stock_UP == True:
                    cheking_stock_UP = False
                    user_order.append("1")
                    finish_renting = True
                    return rent2(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE)
                else:
                    while user != True:
                        print("UP is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                        user_input = int(input(": "))
                        try:
                            print(user_input)
                        except ValueError:
                            print("Please only insert 1, 2, 3, 4")
                            return rent2(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE)
                        if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                            print("Please only insert 1, 2, 3, 4")
                        elif user_input == 1:
                            user = True
                            return rent2(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE)
                        elif user_input == 2:
                            user = True
                            return menu()
                        elif user_input == 3:
                            user = rental_report()
                        elif user_input == 4:
                            user = True
                            print("Thanks for stopping by!\n")
                        else:
                            print("Unknown Error Occur")
            
def menu():
    user_exit = False
    while user_exit != True:
        print("Welcome to Movie Rental System!")
        print("Please pick the opintion you trying to do")
        print("0.Search 1.Rent 2.Return 3.Generate Rental Report 4.Exit\n")
        user_input = int(input("Your choice boss: \n"))
        if user_input == 1:
            rent(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE)
            user_exit = True


        if user_input == 4:
            user_exit = True
            print("Thanks for stopping by!\n")
    else:
        print("Thanks for stopping by!\n")

  


def returns():
    pass

def rental_report():
    pass

cheking_stock_UP = True
cheking_stock_Hunger_Game = True
cheking_stock_hachi = True
cheking_stock_Alex = True
cheking_stock_FATE = True
user_exit = False
user_order = []
movie_list = ["UP","The Hunger Game", "Hachi: A Dog's Tale","Alex's Autobiography", "FATE"]
movie_prize = ["UP                                    10$","The Hunger Game                       15$", "Hachi: A Dog's Tale                   30$","Alex's Autobiography                   1$", "FATE                                  20$"]
while user_exit != True:
    print("Welcome to Movie Rental System!")
    print("Please pick the opintion you trying to do")
    print("0.Search 1.Rent 2.Return 3.Generate Rental Report 4.Exit\n")
    user_input = int(input("Your choice boss: \n"))
    if user_input == 1:
        rent(movie_prize, user_order, movie_list, cheking_stock_UP, cheking_stock_Hunger_Game, cheking_stock_hachi, cheking_stock_Alex, cheking_stock_FATE)
        user_exit = True


    if user_input == 4:
        user_exit = True
else:
    print("Thanks for stopping by!\n")