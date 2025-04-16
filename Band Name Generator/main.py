# Step1: Welcome the user to the program
print("Welcome to Band Name Generator!!")

# Step2: Ask user for their city and pet names
city_name = input("What's the name of the city you grew up in? ").capitalize()
pet_name = input("What's your pet's name? ").capitalize()

# Step3: Combine both inputs and display the result as band name.
print(f'Your band name is: {city_name} {pet_name}')
