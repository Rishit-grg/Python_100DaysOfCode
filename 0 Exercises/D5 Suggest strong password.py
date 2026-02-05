import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# .................................... 
# import string

# letters = list(string.ascii_letters)
# numbers = list(string.digits)
# symbols = list("!#$%&()*+")

# string module details - https://github.com/python/cpython/blob/3.14/Lib/string/__init__.py
# .....................................

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

# .................My way....................................................................
l = 0 
n = 0 
s = 0
# while l < nr_letters or n < nr_numbers or s < nr_symbols:
#     choice = random.randint(0,2)
#     if choice == 0 and l < nr_letters:
#         password.append(random.choice(letters))
#         l+=1
#     elif choice == 1 and n < nr_numbers:
#         password.append(random.choice(numbers))
#         n+=1
#     elif choice == 2 and s < nr_symbols:
#         password.append(random.choice(symbols))
#         s+=1




# ...................Better way is to use random.shuffle.....................................
0
while l < nr_letters:
    password.append(random.choice(letters))
    l+=1
while n < nr_numbers:
    password.append(random.choice(numbers))
    n+=1
while s < nr_symbols:
    password.append(random.choice(symbols))
    s+=1

random.shuffle(password) #..................... # IMP !!**!!*!****!!!!!**!*!!!!*!*!!*!*!!!**!

print("Suggested Password is - ","".join(password))   # without this join func lists are printed like ['a', 'b', 'c', 'd', 'e']
