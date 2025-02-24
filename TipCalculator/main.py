print('Welcome to the tip calculator! ')

bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

# converting tip to percentage
tip_as_percent = tip / 100

# # multipliying the  with tippercentage with original bill
total_tip_amount = tip_as_percent * bill

# adding total tip amount to the original bill
total_bill =  total_tip_amount + bill

# splitting bill to each person
bill_per_person = total_bill / people

# rounding the final amount
final_amount = round(bill_per_person, 2)

print(f'Each person should pay: {final_amount}')
