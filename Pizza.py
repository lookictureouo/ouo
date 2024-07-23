def menu():
    #You should display a menu here! Make it look pretty!
    print("What you want in your pizza?")
    order()
    


def order():
    x = 0
    if item is not None:
        item = item
    else:
        item = 0
    finish_order = False
    print(the_menu[item])
    while finish_order != True:
        x = input("1.Next 2.Back 3.Done 4.Order: " )
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
        elif x == 4:
            orderlist.append(item) 
        else:
            print("An error has occurred, check what have you typed or context us by xxx-xxx-xxxx")
            return order()

def listchecking():
    user_finish_checking = False
    x = 0
    listLength = len(orderlist + 1)
    for i in orderlist:
        for e in listLength:
            print(e)
            print(i)
    while user_finish_checking == False:
        x = input("0.Done @.Back or type the number of the item you want to remove: ")
        if x == 0:
            user_finish_checking = True
            total()
        elif x == "@":
            order()
        else:
            orderlist.pop(x - 1)
	

def total():
        cost = 0
        for i in orderlist:
            if i == "Cheese": 
                cost = cost + 2
            elif i == "Tomato Sauce":
                cost = cost + 1
            elif i == "Pineapple":
                cost = cost + 5
            elif i == "Olive":
                cost = cost + 3
            elif i == "Onion":
                cost = cost + 2
            elif i == "Broccoli":
                cost = cost + 3
            elif i == "Cauliflower":
                cost = cost + 3
            elif i == "Artichokes":
                cost = cost + 4
            elif i == "Pepperoni":
                cost = cost + 4
            elif i == "Sausage":
                cost = cost + 6
            elif i == "Bacon":
                cost = cost + 3
            elif i == "Mushroom":
                cost = cost + 1
        print(cost) 

orderlist = []
the_menu = ["Cheese","Tomato Sauce","Pineapple","Olive","Onion","Broccoli","Artichokes","Cauliflower","Pepperoni","Sausage","Bacon","Mushroom"]
user_finish_checking = False
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