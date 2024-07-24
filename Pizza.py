def menu():
    #You should display a menu here! Make it look pretty!
    print("What you want in your pizza?")
    order()
    


def order(the_menu, orderlist,the_menu_order):
    x = 0
    finish_order = False
    for i in the_menu:
        print(i)
    while finish_order != True:
        x = input("0.Done or Insert the ID of the food to order: " )
        if x <= 12 and x > 0:
            orderlist.append(the_menu_order(x-1))
        elif x == 0:
            finish_order = True
            total()
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
	

def total(orderlist):
    
        cost = 0
        for i in orderlist:
            if i == the_menu_order(0): 
                cost += 2
            elif i == the_menu_order(1):
                cost = cost + 1
            elif i == the_menu_order(2):
                cost = cost + 5
            elif i == the_menu_order(3):
                cost = cost + 3
            elif i == the_menu_order(4):
                cost = cost + 2
            elif i == the_menu_order(5):
                cost = cost + 3
            elif i == the_menu_order(6):
                cost = cost + 3
            elif i == the_menu_order(7):
                cost = cost + 4
            elif i == the_menu_order(8):
                cost = cost + 4
            elif i == the_menu_order(9):
                cost = cost + 6
            elif i == the_menu_order(10):
                cost = cost + 3
            elif i == the_menu_order(11):
                cost = cost + 1
        print(cost) 

orderlist = []
the_menu = ["1. Cheese","2. Tomato Sauce","3. Pineapple","4. Olive","5. Onion","6. Broccoli","7. Artichokes","8. Cauliflower","9. Pepperoni","10. Sausage","11. Bacon","12. Mushroom"]
the_menu_order = ["Cheese","Tomato Sauce","Pineapple","Olive","Onion","Broccoli","Artichokes","Cauliflower","Pepperoni","Sausage","Bacon","Mushroom"]
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