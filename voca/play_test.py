""" Start the vocabulary test game. """
import time
import json
from print_words import print_words
from loading_feature import loading


def start_test(word_list):
    """
    Start the vocabulary test game.
    """
    unit = "unit_" + \
        input("\n> Enter the unit you want to test on (1/2/3...) : ")
    is_unit = print_words(unit)
    i = 1
    correct_answers = 0
    incorrect_answers = 0
    if is_unit:
        print("\n> Starting the test...\n")
        loading()
        for word in word_list[unit]:
            print(f"{i}. {word['word']}")
            answer = input("\n> Enter translation : ")
            if answer == word['meaning']:
                print("\n> Correct!\n")
                correct_answers += 1
            else:
                print(
                    f"\n> Incorrect! The correct answer is: {word['meaning'][::-1]}\n")
                incorrect_answers += 1
            i += 1
            loading()
            time.sleep(0.5)  # Wait for 1.5 seconds
        print("\n> Test completed!\n")

        is_sum = input("\n> Do you want to see the summary? (y/n) : ").lower()
        if is_sum == "y":
            print(f"\n> Correct answers: {correct_answers}")
            print(f"> Incorrect answers: {incorrect_answers}")
            print(f"> Total words: {len(word_list[unit])}")
            print(
                f"> Score: {correct_answers / len(word_list[unit]) * 100:.2f}%\n")
        else:
            print("\n> Thank you for playing!\n")

    else:
        print("\n> Aborting the test...\n")


if __name__ == "__main__":
    # Example usage
    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)
    start_test(words_list)
