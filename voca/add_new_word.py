""" A Module to add a new word to the vocabulary JSON file. """

import json
import os


def add_word(word, meaning, unit):
    """ Check if the file exists. """
    if not os.path.exists("vocabulary.json"):
        # If it doesn't exist, create an empty list
        words_list = {"unit_1": [{"word": word, "meaning": meaning}]}

        with open("vocabulary.json", "w", encoding="utf-8") as file:
            json.dump(words_list, file, indent=4)
    else:
        # If it exists, read the existing words
        with open("vocabulary.json", "r", encoding="utf-8") as file:
            words_list = json.load(file)

        user_unit = "unit_" + str(unit)
        flag = 0

        for u in words_list:
            if u == user_unit:
                # Check if the word already exists in the unit
                for word_dict in words_list[u]:
                    if word_dict["word"].lower() == word.lower():
                        print("\n> Word already exists in the unit.\n")
                        flag = 1
                        return None
                words_list[u].append({"word": word.lower(), "meaning": meaning})
                flag = 1

        if flag == 0:
            print("\n> Unit does not exist. Creating a new unit...\n")
            # Create a new unit and add the word
            words_list[user_unit] = [{"word": word, "meaning": meaning}]

    # Write the updated words back to the file
    with open("vocabulary.json", "w", encoding="utf-8") as file:
        json.dump(words_list, file, indent=4)

    print("\n> Word added successfully!\n")


if __name__ == "__main__":
    add_word("DDD", "a representative form or pattern", 1)
