# Bmi Calculator:
    # The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
        #  - weight / height ** 2 - (weight divided by height to the power of 2)

# Datatypes of variables
# weight - datatype - float
# height - datatype - float
# input() - by default returns string(text)

# Steps:
# 1. Welcome note
print("Welcome to BMI calculator")

# 2. Get the weight of user as an input - convert it into float
user_weight = float(input("What's your weight? "))

# 3. Get the height of user as an input - convert it into float
user_height = float(input("What's your height? "))

# 4. Apply the formula
bmi = user_weight / (user_height ** 2)

# 5. Print the result in terminal
print(f"Your Body Mass Index is: {round(bmi, 2)}")
