""" Start the vocabulary training game. """
import random
import time
import json


def play_the_game(word_list, word1, word2):
    """ Play the vocabulary training game with the given word list and range. """
    is_playing = True
    flag = 0
    start = 0
    end = 0
    if word1:
        last_word = 'temp'
        for word in word_list:
            if word1 == word['word'] or word2 == word['word']:
                flag += 1
                if flag == 1:
                    start = word_list.index(word)
                elif flag == 2:
                    end = word_list.index(word)

        if flag == 2:  # If both words are found
            word_range = end - start + 1
            while is_playing:  # Loop until the user decides to stop or all words are shown 7 times
                # Randomly select a word from the range
                random_num = random.randint(start, end)
                # Avoid showing the same word consecutively
                if last_word != word_list[random_num]['word']:
                    # Check if the word has been shown 7 times
                    if word_list[random_num]['counter'] != 7:
                        print(f"\n> Word: {word_list[random_num]['word']}")
                        # Update last_word
                        last_word = word_list[random_num]['word']
                        time.sleep(3)  # Wait for 3 seconds
                        print(f"> Meaning: {word_list[random_num]['meaning']}")
                        time.sleep(1.5)  # Wait for 1.5 seconds
                        # Increment the word counter
                        word_list[random_num]['counter'] += 1
                    else:  # If the word has been shown 7 times, decrement the word_range flag
                        word_range -= 1
                    if word_range == 0:  # If all words have been shown 7 times, exit the loop
                        print("\n> All words have been shown 7 times.\n")
                        is_playing = False  # Exit the loop
        else:  # If the words are not found in the list
            print("\n> Words not found in the list.\n")
            return False
    else:  # If no specific range is provided, show all words
        last_word = 'temp'
        word_range = len(word_list)
        while is_playing:
            # Randomly select a word from the list
            random_num = random.randint(0, len(word_list) - 1)
            # Avoid showing the same word consecutively
            if last_word != word_list[random_num]['word']:
                # Check if the word has been shown 7 times
                if word_list[random_num]['counter'] != 7:
                    print(f"\n> Word: {word_list[random_num]['word']}")
                    # Update last_word
                    last_word = word_list[random_num]['word']
                    time.sleep(3)
                    print(f"> Meaning: {word_list[random_num]['meaning']}")
                    time.sleep(1.5)
                    # Increment the word counter
                    word_list[random_num]['counter'] += 1
                else:  # If the word has been shown 7 times, decrement the word_range flag
                    word_range -= 1
                if word_range == 0:
                    print("\n> All words have been shown 7 times.\n")
                    is_playing = False

    print("\n> Exiting the game...\n")


if __name__ == "__main__":
    # Example usage
    with open("vocabulary.json", "r", encoding="utf-8") as file:
        word_list1 = json.load(file)
    play_the_game(word_list1, 'apple', 'cherry')
