import string
import random

print("Welcome to the PyPassword Generator!")

# using string module
letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

# Getting user inputs on letters, symbols and numbers
no_letters = int(input("How many letters would you like in your password? "))
no_symbols = int(input("How many symbols would you like? "))
no_numbers = int(input("How many numbers would you like? "))

password = []
for char in range(0, no_letters):
    password.append(random.choice(letters))
for symbol in range(0, no_symbols):
    password.append(random.choice(symbols))
for num in range(no_numbers):
    password.append(random.choice(numbers))

# converting list to string
random.shuffle(password)
final_password = "".join(password)
print(final_password)
