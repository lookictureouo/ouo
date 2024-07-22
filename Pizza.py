def menu():
    #You should display a menu here! Make it look pretty!
    print("What you want in your pizza?")
    order()
    


def order():
    x = 0
    if do_not_set_0 != False:
        item = item
    else:
        item = 0
    finish_order = False
    print(the_menu[item])
    while finish_order != True:
        x = input("1.Next 2.Back 3.Done: " )
        if x == 1:
            item = item + 1
            do_not_set_0 = True
            return order()
        elif x == 2: 
            item = item - 1
            do_not_set_0 = True
            return order()
        elif x == 3:
            total()
        else:
            print("An error has occurred, check what have you typed or context us by xxx-xxx-xxxx")
            return order()


	

def total(order_list):
    #look through their order list and calculate the cost
    cost = 0
    return cost
do_not_set_0 = False 
the_menu = ["Cheese","Tomato Sauce","Pineapple","Olive","onion","Broccoli","Artichokes","Cauliflower","Pepperoni","Sausage","Bacon","Mushroom"]
user_exit = False
while user_exit != True:
    print("Welcome to the Pizza Store!")
    print("Please pick what you would like to do!")
    print("1.Menu 2.Order 3.Calculate Total 4.Exit \n")
    user_input = int(input("Your choice boss: \n"))
    if user_input == 1:
        menu()
        user_exit = True
    if user_input == 4:
        user_exit = True
        print("Thanks for stopping by!\n")
    #Your code can go here
    #You may want to add to this if statement 