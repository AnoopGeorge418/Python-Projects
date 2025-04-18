print("Welcome to Tip Calculator!")

amount = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give (10, 12, 15)? "))
people = int(input("How many people to split the bill?: "))

tip = tip_percentage / 100 
total_tip_amount = amount * tip
total_bill = amount + total_tip_amount

bill_per_person = total_bill / people

print(f"Each person should pay: ${bill_per_person:.2f}")
