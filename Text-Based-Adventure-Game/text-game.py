class AdventureGame:
    def __init__(self):
        self.current_chapter = 1

    def start_game(self):
        print("Welcome to the Lost City of Eldoria!")
        self.chapter_one()

    def chapter_one(self):
        print("Chapter 1: The Jungle Trek")
        print("You stand at the edge of a dense jungle. What will you do?")
        choice = input("Options: (1) Take the main path (2) Take the narrow path\n")
        if choice == "2":
            print("You find a hidden trail that leads you safely through the jungle.")
            self.current_chapter = 2
            self.chapter_two()
        else:
            print("You get lost in the dense jungle. Try again.")
            self.chapter_one()

    def chapter_two(self):
        print("Chapter 2: The Ancient Ruins")
        print("You arrive at the ruins of an ancient temple. What will you do?")
        choice = input("Options: (1) Examine the symbols on the walls (2) Look for hidden mechanisms\n")
        if choice == "1":
            print("The symbols reveal a clue to unlocking the temple entrance.")
            self.current_chapter = 3
            self.chapter_three()
        else:
            print("You can't find any mechanisms. Try again.")
            self.chapter_two()

    def chapter_three(self):
        print("Chapter 3: The Temple of Trials")
        print("You face a series of trials inside the temple. What will you do?")
        choice = input("Options: (1) Face the trials head-on (2) Look for alternative ways\n")
        if choice == "2":
            print("You find hidden passages that help you avoid some of the trials.")
            self.current_chapter = 4
            self.chapter_four()
        else:
            print("You struggle through the trials but manage to proceed.")
            self.current_chapter = 4
            self.chapter_four()

    def chapter_four(self):
        print("Chapter 4: The Guardian's Challenge")
        print("You encounter the Guardian. What will you do?")
        choice = input("Options: (1) Fight the Guardian (2) Answer the Guardian's riddles\n")
        if choice == "2":
            print("You answer the riddles correctly and gain access to Eldoria.")
            self.current_chapter = 5
            self.chapter_five()
        else:
            print("The Guardian defeats you. Try again.")
            self.chapter_four()

    def chapter_five(self):
        print("Chapter 5: The Lost City of Eldoria")
        print("You reach the Lost City. What will you do?")
        choice = input("Options: (1) Explore the city (2) Search for hidden treasures\n")
        if choice == "2":
            print("You uncover the hidden secrets of Eldoria.")
            self.end_game()
        else:
            print("You explore the city and admire its beauty.")
            self.end_game()

    def end_game(self):
        print("Congratulations! You have successfully navigated the Lost City of Eldoria.")
        print("Thank you for playing!")

if __name__ == "__main__":
    game = AdventureGame()
    game.start_game()
