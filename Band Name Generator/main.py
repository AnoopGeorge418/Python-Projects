# Step 1 : Welcome statement
print("Welcome to Band Name Generator")

# Step 2 : Get users birth city
city_name = input("What's your birth city name? ").capitalize()

# Step 3 : Get users pets name
pet_name = input("What's your pets name? ").capitalize()

# step4 : Concatenating  step 2 and 3 and display the result
print(f"Your Band Name is: {city_name + " " + pet_name}")
