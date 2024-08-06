user_input = int(input("Choose a number that equal or higher than 0: "))
if user_input < 0 :
    print("please choose a number that equal or higher than 0")
else:
    for result in range(0, user_input + 1):
        print(result)
