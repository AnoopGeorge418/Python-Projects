# Treasure Island - Is game to find the treasure that is hidden in a island. - Uses If conditions to select the correct path to reach the treasure island and collect the Treasure.

# steps:
# ascii image of trasure
print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

# 1. Welcome note
print("Welcome to Treasure Island Game")
ready_or_not = input("You are in a mission to find the Treasure Island, Are You Ready? (Yes or No): ").lower()
if ready_or_not == 'yes':
    wait_or_swim = input("You've come to a lake in the middle of the lake there is an island, Type 'Wait' to wait for boat or 'Swim' to swim to the island: ").lower()
    if wait_or_swim == 'wait':
        choice = input("You've arrived the island unharmed. There is a house with 3 doors (red, blue, yellow) choose any one: ").lower()
        if choice == 'red':
            print("Oops! You've entered a room full of fire. GAME OVER!!")
        elif choice == 'blue':
            print("Oops! You've entered a room full of beasts. GAME OVER!!")
        elif choice == 'yellow':
            print("Hooraay!! You have found the Treasure..")
        else:
            print("Make sure to Choose from ('red', 'blue', or 'yellow')")
    elif wait_or_swim == 'swim':
        print("Oops! You got attacked by angry trout. GAME OVER!!")
    else:
        print("Make sure to choose from ('Wait' or 'Swim')")
elif ready_or_not == 'no':
    print('GAME OVER!!!!')

