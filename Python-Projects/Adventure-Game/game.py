print('Welcome to the game! ')
name = input('What is your name? ')
age = int(input('What is your age? '))

health = 10

if age >= 18:
    print('You are old enough!')

    weapon = input('Pick a weapon (sword/baton): ').lower()
    if weapon not in ['sword', 'baton']:
        weapon = ''  # Ensures weapon is set to an empty string if invalid option is chosen
    
    wants_to_play = input('Do you want to play? (yes/no): ').lower()
    if wants_to_play == 'yes':
        print(f'You are starting with {health} health.')
        print('Let\'s play!')

        left_or_right = input('First choice... (left/right): ').lower()
        if left_or_right == 'left':
            ans = input('Nice, you followed a path and reached a lake... Do you swim across or go around (across/around)? ').lower()
            if ans == 'around':
                print('You went around and reached the other side of the lake.')
            elif ans == 'across':
                print('You managed to get across, but got bitten by a fish and lost 5 health.')
                health -= 5

            ans = input('You noticed a house and a river. Which do you go to (river/house)? ').lower()
            if ans == 'house':
                print('You go to the house and are greeted by the owner... He doesn\'t like you and you lose 5 health.')
                health -= 5
                if health <= 0:
                    print('You now have 0 health and you lose the game...')
                else:
                    print('You have survived...')
            else:
                print('You fell in the river and lost.')
        else:
            print('You fell down and lost...')
    else:
        print('See ya...')
else:
    print('You are not old enough to play!')
