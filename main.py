""" Main module for the English vocabulary game. """
import time
from print_options import print_game_options
from loading_feature import loading
from create_game import create_game
from edit_controller import load_edit_controller
from print_words import print_words

def main():
    """ Main function to start the English vocabulary game. """
    is_playing = True
    print("\nWelcome to the English Vocabulary Game!")
    loading()
    time.sleep(1)
    print("\nMain Menu:")
    print_game_options()
    while is_playing:
        choice = input("\n> Enter your choice (1/2/3...), 3 for menu : ")
        if choice == "1":
            #print("\n> Starting game...\n")
            time.sleep(1)
            create_game()
        elif choice == "2":
            print("\n> Starting edit mode...\n")
            time.sleep(1)
            load_edit_controller()
        elif choice == "3":
            print("\n> Showing options...\n")
            time.sleep(1)
            print_game_options()
        elif choice == "4":
            print("\n> Showing all words...\n")
            time.sleep(1)
            print_words()
        elif choice == "5":
            print("\n> Exiting the game...\n")
            time.sleep(1)
            is_playing = False
        else:
            print("\n> Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
