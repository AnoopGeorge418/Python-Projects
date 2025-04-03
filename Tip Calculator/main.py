# Tip Calculator - A Program that lets you split the bill amoungs people as per the tip they are giving.

# total_bill_amount - datatype - float
# tip - datatype - int
# people - datatype - int
# input() - return string(text)by default

# Steps:
# 1. Welcome note
print("Welcome to Tip Calculator!")

# 2. Get the total bill amount from user as input - convert into float
total_bill = float(input("Enter the total bill amount: "))

# 3. Ask for the tip percentage they like to pay (10, 12, or 15) - convert this into int
tip = int(input("Enter the tip percentage (10, 12, or 15): "))

# 4. Number of people = convert to int
people = int(input("Number of people: "))

# 5. Perform math
# lets convert the tip into percentage
tip_in_percentage = tip / 100

# multiply the tip_in_percentage with actual user bill
bill_amount = total_bill * tip_in_percentage

# add the actaul user bill with bill_amount
bill = total_bill + bill_amount

# divide the bill per number of people
bill_per_people = bill / people

# 6. Display the result in the terminal
print(f'Your total bill including tip as per {people} people is {bill_per_people}')
print(f"Each person has to pay {bill_per_people} amount.")