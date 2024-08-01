def menu():
    pass

def search():
    pass

def rent(movie_prize, user_order, movie_list):
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
    return rent2(movie_prize, user_order, movie_list, inventory)

def rent2(movie_prize, user_order, movie_list, inventory):
    finish_renting = False
    user = False
    print("Do you want to rent 0.rental_report 1.UP 2.The Hunger Game 3.Hachi: A Dog's Tale 4.Alex's Autobiography 5.FATE 6.Back to menu 7.Exit")
    user_input = int(input(": "))
    try:
        print(user_input)
    except ValueError:
        print("Please only insert 0, 1, 2, 3, 4, 5, 6, 7") #checking user only insert 1,2 3,4,5,6,7
    if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 5 and user_input != 6 and user_input != 7:
        print("Please only insert 0, 1, 2, 3, 4, 5, 6, 7") #checking user only insert 1,2 3,4,5,6,7
        return rent2(movie_prize, user_order, movie_list, inventory)
    else:
        while finish_renting !=  True:
            if user_input == 0: #Report
                rental_report()
            elif user_input == 1: #For UP
                for stuff in inventory:
                    if stuff == "1":
                        user_order.append("1") #Add UP in User inventory
                        inventory.remove("1") #Remove UP in inventory
                        finish_renting = True
                        return rent2(movie_prize, user_order, movie_list, inventory)
                    else:
                        pass

                    while user != True:
                                print("UP is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                                user_input = int(input(": "))
                                try:
                                    print(user_input)
                                except ValueError:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                elif user_input == 1:
                                    user = True
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                elif user_input == 2:
                                    user = True
                                    return menu()
                                elif user_input == 3:
                                    user = rental_report()
                                elif user_input == 4:
                                    user = True
                                    print("Thanks for stopping by!\n")
                                else:
                                        print("Unknown Error Occur") #For testing
            elif user_input == 2: #For Hunger Game
                for stuff in inventory:
                    if stuff == "2":
                        user_order.append("2") #Add Hunger Game in User inventory
                        inventory.remove("2") #Remove Hunger Game in inventory
                        finish_renting = True
                        return rent2(movie_prize, user_order, movie_list, inventory)
                    else:
                        pass

                    while user != True:
                                print("The Hunger Game is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                                user_input = int(input(": "))
                                try:
                                    print(user_input)
                                except ValueError:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                elif user_input == 1:
                                    user = True
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                elif user_input == 2:
                                    user = True
                                    return menu()
                                elif user_input == 3:
                                    user = rental_report()
                                elif user_input == 4:
                                    user = True
                                    print("Thanks for stopping by!\n")
                                else:
                                        print("Unknown Error Occur") #For testing
            elif user_input == 3: #For Hachi: A Dog's Tale
                for stuff in inventory:
                    if stuff == "3":
                        user_order.append("3") #Add Hachi: A Dog's Tale in User inventory
                        inventory.remove("3") #Remove Hachi: A Dog's Tale in inventory
                        finish_renting = True
                        return rent2(movie_prize, user_order, movie_list, inventory)
                    else:
                        pass

                    while user != True:
                                print("Hachi: A Dog's Tale is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                                user_input = int(input(": "))
                                try:
                                    print(user_input)
                                except ValueError:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                elif user_input == 1:
                                    user = True
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                elif user_input == 2:
                                    user = True
                                    return menu()
                                elif user_input == 3:
                                    user = rental_report()
                                elif user_input == 4:
                                    user = True
                                    print("Thanks for stopping by!\n")
                                else:
                                        print("Unknown Error Occur") #For testing
            elif user_input == 4: #For Alex's Autobiography
                for stuff in inventory:
                    if stuff == "4":
                        user_order.append("4") #Add Alex's Autobiography in User inventory
                        inventory.remove("4") #Remove Alex's Autobiography in inventory
                        finish_renting = True
                        return rent2(movie_prize, user_order, movie_list, inventory)
                    else:
                        pass

                    while user != True:
                                print("Alex's Autobiography is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                                user_input = int(input(": "))
                                try:
                                    print(user_input)
                                except ValueError:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                elif user_input == 1:
                                    user = True
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                elif user_input == 2:
                                    user = True
                                    return menu()
                                elif user_input == 3:
                                    user = rental_report()
                                elif user_input == 4:
                                    user = True
                                    print("Thanks for stopping by!\n")
                                else:
                                        print("Unknown Error Occur") #For testing
            elif user_input == 5: #For FATE
                for stuff in inventory:
                    if stuff == "5":
                        user_order.append("5") #Add FATE in User inventory
                        inventory.remove("5") #Remove FATE in inventory
                        finish_renting = True
                        return rent2(movie_prize, user_order, movie_list, inventory)
                    else:
                        pass

                    while user != True:
                                print("FATE is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                                user_input = int(input(": "))
                                try:
                                    print(user_input)
                                except ValueError:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                                    print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                                elif user_input == 1:
                                    user = True
                                    return rent2(movie_prize, user_order, movie_list, inventory)
                                elif user_input == 2:
                                    user = True
                                    return menu()
                                elif user_input == 3:
                                    user = rental_report()
                                elif user_input == 4:
                                    user = True
                                    print("Thanks for stopping by!\n")
                                else:
                                        print("Unknown Error Occur") #For testing
            elif user_input == 6: #Menu
                menu()
            elif user_input == 7: #EXIT
                print("Thanks for stopping by!\n")
            else:
                print("Unknown Error Occur") #For testing


def menu():
    user_exit = False
    while user_exit != True:
        print("Welcome to Movie Rental System!")
        print("Please pick the opintion you trying to do")
        print("0.Search 1.Rent 2.Return 3.Generate Rental Report 4.Exit\n")
        user_input = int(input("Your choice boss: \n"))
        if user_input == 1:
            rent(movie_prize, user_order, movie_list)
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

user_exit = False
inventory = ["1","2","3","4","5"]
user_order = []
movie_list = ["UP","The Hunger Game", "Hachi: A Dog's Tale","Alex's Autobiography", "FATE"]
movie_prize = ["UP                                    10$","The Hunger Game                       15$", "Hachi: A Dog's Tale                   30$","Alex's Autobiography                   1$", "FATE                                  20$"]
while user_exit != True:
    print("Welcome to Movie Rental System!")
    print("Please pick the opintion you trying to do")
    print("0.Search 1.Rent 2.Return 3.Generate Rental Report 4.Exit\n")
    user_input = int(input("Your choice boss: \n"))
    if user_input == 1:
        rent(movie_prize, user_order, movie_list)
        user_exit = True


    if user_input == 4:
        user_exit = True
else:
    print("Thanks for stopping by!\n")