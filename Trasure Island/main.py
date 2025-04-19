print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go ")
left_or_right = input('Type "left" or "right": ')
if left_or_right.lower() == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across: ')
    if wait_or_swim.lower() == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors: ")
        red_yellow_blue = input("One red, one yellow and one blue. Which colour do you choose? ")
        if red_yellow_blue.lower() == 'red':
            print("It's a room full of fire. Game Over.")
        elif red_yellow_blue.lower() == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif red_yellow_blue.lower() == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("One red, one yellow and one blue. Which colour do you choose?")
    elif wait_or_swim.lower() == 'swim':
        print("You get attacked by an angry trout. Game Over.")
    else:
        print('Type "wait" to wait for a boat. Type "swim" to swim across.')
elif left_or_right.lower() == 'right':
    print("You fell into a hole. Game Over")
else:
    print('Type "left" or "right')
