# Treasure Island - Is game to find the treasure that is hidden in a island. - Uses If conditions to select the correct path to reach the treasure island and collect the Treasure.

# steps:
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

