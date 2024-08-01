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
    found = False
    print("Do you want to rent 0.rental_report 1.UP 2.The Hunger Game 3.Hachi: A Dog's Tale 4.Alex's Autobiography 5.FATE 6.Back to menu 7.Exit")
    user_input = int(input(": "))
    try:
        print(user_input)
    except ValueError:
        print("Please only insert 0, 1, 2, 3, 4, 5, 6, 7") #checking user only insert 1,2 3,4,5,6,7
    if user_input != 0 and user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 5 and user_input != 6 and user_input != 7:
        print("Please only insert 0, 1, 2, 3, 4, 5, 6, 7") #checking user only insert 1,2 3,4,5,6,7
        return rent2(movie_prize, user_order, movie_list, inventory)
    else:
        while finish_renting !=  True:
            if user_input == 0: #Report
                rental_report(user_order)
            elif user_input in [1, 2, 3, 4, 5]:
                for stuff in inventory:
                    if stuff == str(user_input):
                        user_order.append(stuff)  # Add movie to User inventory
                        inventory.remove(stuff)   # Remove movie from inventory
                        finish_renting = True
                        found = True
                        return rent2(movie_prize, user_order, movie_list, inventory)
                                      
                if not found:
                    print(f"Movie {user_input} is out of stock, 1.rent other movie 2.menu 3.rental_report 4.Exit")
                    user_input = int(input(": "))
                    try:
                        print(user_input)
                    except ValueError:
                        print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4
                        return rent2(movie_prize, user_order, movie_list, inventory)
                    while user != True:
                        if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                            print("Please only insert 1, 2, 3, 4") #checking user only insert 1,2 3,4                
                        elif user_input == 1:
                            user = True
                            return rent2(movie_prize, user_order, movie_list, inventory)
                        elif user_input == 2:
                            user = True
                            return menu()
                        elif user_input == 3:
                            user = True
                            return rental_report(user_order)
                        elif user_input == 4:
                            user = True
                            print("Thanks for stopping by!!!!!!!!!!!!\n")
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

def rental_report(user_order):
    for i in user_order:
        print(i)

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