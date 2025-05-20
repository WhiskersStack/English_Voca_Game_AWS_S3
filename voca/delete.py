"""
Delete a word from the vocabulary
"""
import json
import os


def delete_word(word, unit):
    """
    Delete a word from the vocabulary
    """
    if not os.path.exists("vocabulary.json"):
        print("\n> Vocabulary file does not exist.\n")
        return

    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)

    user_unit = "unit_" + str(unit)

    for w in words_list[user_unit]:
        if w["word"] == word.lower():
            words_list[user_unit].remove(w)
            with open("vocabulary.json", "w", encoding="utf-8") as file:
                json.dump(words_list, file, indent=4)
                print("\n> Word deleted successfully!\n")
            print("\n> Word deleted successfully!\n")
            return

    print("\n> Word not found in the vocabulary.\n")


if __name__ == "__main__":
    # Example usage
    delete_word("demo", 1)
