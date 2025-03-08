print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
print('You are at a cross road. Where do you want to go?')

leftRight = input('Type "left" or "right": ').lower()
if leftRight == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    waitSwim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if waitSwim == 'wait':
        print("You've arrived at the island unharmed. There is a house with 3 doors. One Red, Yellow and Blue")
        color = input('Which color do you choose? ').lower()
        if color == 'red':
            print("It's room full of fire, GAME OVER.")
        elif color == 'yellow':
            print('You found the treasure! YOU WIN!')
        else:
            print('You enter a room of beasts. GAME OVER.')
    else:
        print('You get attacked by an angry trout. GAME OVER.')
else:
    print('You fell into a hole. GAME OVER.')
