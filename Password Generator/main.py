# Password Generator - Generating random password which contains letters, numbers, and symbols

import string
import random

# creating lists of numbers, symbols, letters using string module
letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)

# User inputs for determine the number of letters, symbols, and numbers to be in password
n_letters = input("How many letters you want in your password? ")
n_symbols = input("How many symbols you want in your password? ")
n_numbers = input("How many numbers you want in your password? ")

# converting input string to integers
n_letters = int(n_letters)
n_symbols = int(n_symbols)
n_numbers = int(n_numbers)

# selecting letters, numbers, and symbols randomly from the list and storing it in a new list
passwords = []
for letter in range(0, n_letters):
    passwords.append(random.choice(letters))

for symbol in range(0, n_symbols):
    passwords.append(random.choice(symbols))

for number in range(0, n_numbers):
    passwords.append(random.choice(numbers))

# shuffle the password
random.shuffle(passwords)

# converting list of shuffled password to string
shuffled_password = ''
for char in passwords:
    shuffled_password += char

print(f'Your password is: {shuffled_password}')