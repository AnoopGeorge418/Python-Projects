print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? '))
tip = int(input('How much tip would you like to give? '))
people = int(input('How many people to split the bill? '))


tip_as_percentage = tip / 100
total_tip_amount = total_bill * tip_as_percentage
total = total_bill + total_tip_amount
bill_per_person = total / people

print(f'Each Person should pay: ${round(bill_per_person, 2)}')