# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# weight / height ** 2 - (weight divided by height to the power of 2)

# datatypes
    # weight - float
    # height - float
    # input() - returns string(in simple terms 'text') by default

# Steps:
# 1. Welcome Note
print("Welcome to BMI Calculator!")

# 2. Get the weight of user using input function and store it in a variable - convert it into float
weight = float(input("What's your weight? "))

# 3. Get the height of user using input function and store it in a variable - convert it into float
height = float(input("What's your height? "))

# 4. Apply the formula
bmi = weight / (height ** 2)

# 5. Display the output in the console.
print(f"Your Body Mass Index is: {round(bmi, 2)}")
