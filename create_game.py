"""
Vocabulary training game
"""

import json
from print_words import print_words
from play_training import play_the_game


def create_game():
    """
    Load words from the vocabulary file, and initialize the game.
    """

    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)

    # Initialize the counter for each word
    for u in words_list:
        for word in words_list[u]:
            word['meaning'] = word['meaning'][::-1]  # Reverse the meaning
            word['counter'] = 0

    play_unit = "unit_" + \
        input("\n> Enter the unit you want to play (1/2/3...) : ")
    is_unit = print_words(play_unit)
    if is_unit:
        is_range = input(
            "\n> Do you want to loop all the words? (y/n) : ").lower()

        if is_range == "n":
            word1 = input("\n> Enter the first word to start from : ")
            word2 = input("\n> Enter the last word to end : ")
            play_the_game(words_list[play_unit], word1, word2)
        else:
            play_the_game(words_list[play_unit], False, False)
    else:
        print("\n> Aborting the game...\n")


if __name__ == "__main__":
    create_game()
