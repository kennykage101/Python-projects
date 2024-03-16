import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy level
# random_password = ''
# for letter in range(0, nr_letters):
#   random_password += letters[random.randint(0,51)]
# for symbol in range(0, nr_symbols):
#   random_password += symbols[random.randint(0,8)]
# for number in range(0, nr_numbers):
#   random_password += numbers[random.randint(0,9)]
# print(random_password)

password = []
for letter in range(0, nr_letters):
    password.append(letters[random.randint(0,51)])
for symbol in range(0, nr_symbols):
    password.append(symbols[random.randint(0,8)])
for number in range(0, nr_numbers):
    password.append(numbers[random.randint(0,9)])
print(password)
random.shuffle(password)
print(password)

random_password = ""
for char in password:
    random_password += char
print(random_password)
