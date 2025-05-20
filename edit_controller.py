"""Edit Controller Module
This module provides a command-line interface for editing vocabulary words."""

from add_new_word import add_word
from update import update_word
from delete import delete_word


def load_edit_controller():
    """
    Load the edit controller modules.
    """
    print("\n> (1) Add a new word")
    print("> (2) Update an existing word")
    print("> (3) Delete a word")
    print("> (4) Exit edit mode")

    choice = input("> Enter your choice (1/2/3/4): ")
    if choice == "1":
        word = input("\n> Enter the word: ")
        meaning = input("> Enter the meaning: ")
        unit = int(input("> Enter the unit number: "))
        add_word(word, meaning, unit)
    elif choice == "2":
        word = input("\n> Enter the word to update: ")
        new_meaning = input("> Enter the new meaning: ")
        unit = int(input("> Enter the unit number: "))
        update_word(word, new_meaning, unit)
    elif choice == "3":
        word = input("\n> Enter the word to delete: ")
        unit = int(input("> Enter the unit number: "))
        delete_word(word, unit)
    elif choice == "4":
        print("\n> Exiting edit mode...\n")
    else:
        print("\n> Invalid choice. Please try again.\n")
        load_edit_controller()


if __name__ == "__main__":
    load_edit_controller()
