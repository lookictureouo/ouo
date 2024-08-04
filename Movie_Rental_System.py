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
    found = False
    print("Do you want to rent 0.rental_report 1.UP 2.The Hunger Game 3.Hachi: A Dog's Tale 4.Alex's Autobiography 5.FATE 6.Menu 7.Exit")
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
                finish_renting = True
                rental_report(user_order)
            elif user_input in [1, 2, 3, 4, 5]:
                for stuff in inventory:
                    if stuff == str(f"{stuff}"):
                        user_order.append(f"{stuff}")  # Add movie to User inventory
                        inventory.remove(f"{stuff}")   # Remove movie from inventory
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
                        valid_inputs = [1, 2, 3, 4]
                        while_break = True
                        while while_break == True:
                            if user_input not in valid_inputs:
                                print("Please only insert 1, 2, 3, 4")  # checking user only inserts 1, 2, 3, 4
                                user_input = int(input(": "))  # Ask for input again if invalid
                            elif user_input == 1:
                                while_break = False
                                return rent2(movie_prize, user_order, movie_list, inventory)
                            elif user_input == 2:
                                while_break = False
                                return menu()
                            elif user_input == 3:
                                while_break = False
                                return rental_report(user_order)
                            elif user_input == 4:
                                while_break = False
                                print("Thanks for stopping by!\n")
                    elif user_input == 6: #Menu
                        menu()
                    elif user_input == 7: #EXIT
                        print("Thanks for stopping by!\n")
                    else:
                        print("Unknown Error Occur") #For testing

def Return():
    pass


def rental_report(user_order):
    price = 0
    if user_order:
        print("_________________________________________________")
        print("Rental Report:")
        for i in user_order:
            if i == "1":
                print("UP                                    10$\n")
                price += 10
            elif i == "2":
                print("The Hunger Game                       15$\n")
                price += 15
            elif i == "3":
                print("Hachi: A Dog's Tale                   30$\n")
                price += 30
            elif i == "4":
                print("Alex's Autobiography                   1$\n")
                price += 1
            elif i == "5":
                print("FATE                                  20$\n")
                price += 20

        print("Total" + "                                    " + f"{price}$")
        print("1.Rent another movie 2. Menu 3. Exit")
        user_input = int(input(": "))
        if user_input == 1:
            rent(movie_prize, user_order, movie_list)
        elif user_input == 2:
            return menu()
        elif user_input == 3:
            print("Thanks for stopping by!\n")

    else:
        print("No movies rented yet.")
        print("1.Rent 2.Menu 3.Exit")
        user_input = int(input(": "))
        if user_input == 1:
            rent(movie_prize, user_order, movie_list)
        elif user_input == 2:
            return menu()
        elif user_input == 3:
            print("Thanks for stopping by!\n")

def menu():
    user_exit = False
    while not user_exit:
        print("Welcome to Movie Rental System!")
        print("Please pick the option you're trying to do")
        print("0.Search 1.Rent 2.Return 3.Generate Rental Report 4.Exit\n")
        user_input = int(input("Your choice boss: \n"))
        if user_input == 1:
            rent(movie_prize, user_order, movie_list)
        elif user_input == 2:
            Return()
        elif user_input == 3:
            rental_report(user_order)
        elif user_input == 4:
            user_exit = True
            print("Thanks for stopping by!\n")


reporting = False
inventory = ["1", "2", "3", "4", "5"]
user_order = []
movie_list = ["UP", "The Hunger Game", "Hachi: A Dog's Tale", "Alex's Autobiography", "FATE"]
movie_prize = ["UP                                    10$","The Hunger Game                       15$", "Hachi: A Dog's Tale                   30$","Alex's Autobiography                   1$", "FATE                                  20$"]
menu() 