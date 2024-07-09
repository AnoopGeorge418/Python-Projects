import random 
import sys 

def random_number_generator(start, end):
    random_number = random.randint(start, end)
    return random_number
     
def main_game():
    try:
        start = int(input('Enter the Starting Number: '))
        end = int(input('Enter the Ending Number: '))
        random = random_number_generator(start, end)
        
        guess = int(input('Enter your Guess: '))
        if guess == random:
            print('Hooray!! you Guessed It correctly')
        elif guess > random:
            print('Oops Guess is Too High!!')
        else:
            print('Oops Guess is Too Low!!')
        
        exit_from_game = input('Do you want to exit from game (y/n): ').lower()
        if exit_from_game == 'y':
            sys.exit()
        else:
            continue_game = input('Do you want to continue the game (y/n): ').lower()
            if continue_game == 'y':
                main_game()
                
    except ValueError:
        print('Make Sure You Enter Numbers...')
    
def main():
    print('Welcome to the Number Guessing Text Based Game!!')
    main_game()    
    
if __name__ == '__main__':
    main()