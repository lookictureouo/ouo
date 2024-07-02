# lst = input("choose a word: ")
# for i in lst:
#     print(i)

# lst = [1,2,3,4,5]
# for i in lst:
#     print(i*i)

# lst = [1,2,3,4,5,6,7,8,9,10]
# lst.reverse()
# for i in lst:
#     print(i)

# lst = ["Alice", "Bob", "Charlie"]
# for i in lst:
#     print("Hello, " + i)

# Question 10:
# number = range(1,11)
# total = 0  # Initialize a variable to store the sum
# for i in number:
#     total += i
# print(total)
# OR
# x = 0
# for i in range(1,11):
#     x = x + i
# print(x)

# Question 11:
# lst = [10, 20, 30, 40, 50]
# for i in lst:
#     if i > 25:
#         print(i)
    
# Question 12:
# txt = input(str("Write a sentence: "))
# x = txt.split()
# for i in x:
#     print(i)


# txt = str(input("Write a sentence: "))
# vowels = 0
# for i in txt:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i =="A" or i =='E' or i =='I' or i =='O' or i =='U':
#         vowels+=1
# print(vowels)

v = ["a","e","i","o","u"]
txt = str(input("Write a sentence: "))
vowels = 0
for i in txt:
    if i.lower() in v:
        vowels+=1
print(vowels)




    
