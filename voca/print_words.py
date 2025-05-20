""" Printing all the words. """

import json
import os


def print_words(user_unit=None):
    """
    Print all the words in the vocabulary
    """
    if not os.path.exists("vocabulary.json"):
        print("\n> Vocabulary file does not exist.\n")
        return

    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)

    if user_unit:
        # If a specific unit is provided, print only that unit
        if user_unit in words_list:
            print(f"\n{user_unit}:")
            for word in words_list[user_unit]:
                print(f"  - {word['word']}")
        else:
            print(f"\n> Unit {user_unit} does not exist.\n")
            return False
        
        return True
        
    for unit, words in words_list.items():
        print(f"\n{unit}:")
        for word in words:
            print(f"  - {word['word']}: {word['meaning']}")


if __name__ == "__main__":
    print_words()
