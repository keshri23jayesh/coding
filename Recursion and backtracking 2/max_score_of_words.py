# https://www.youtube.com/watch?v=XtmW3a8Q9M4&list=PL3UlF_QlQi8xyUGvQO0pHnX64YCt76j2E&index=3
# My approach

import copy


def get_score(new_arr):
    temp_map = copy.deepcopy(char_map)
    score = 0
    for word in new_arr:
        for letter in list(word):
            if temp_map.get(letter) and temp_map.get(letter) > 0:
                temp_map[letter] -= 1
            else:
                return 0
        for letter in list(word):
            score += words_arr[ord(letter) - 97]
    return score


def select_words(new_arr, words):
    if not words:
        if not new_arr:
            return
        score = get_score(new_arr)
        if score > 0:
            score_map[score] = str(new_arr)
        return

    first_elem = words[0]
    rest_arr = words[1:]

    select_words(new_arr, rest_arr)
    new_arr.append(first_elem)
    select_words(new_arr, rest_arr)
    new_arr.pop()


score_map = {}

given_words = ['dog', 'cat', 'dad', 'good']

char_map = {
    'a': 1,
    'b': 1,
    'c': 1,
    'd': 3,
    'g': 1,
    'o': 2
}

words_arr = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

select_words([], given_words)
print(score_map)


# Teacher Approach


def max_score_of_words(given_words, index, score, char_map):
    # Base case: end of word list
    if index == len(given_words):
        return 0

    # Option 1: Skip the current word
    score_no = max_score_of_words(given_words, index + 1, score, char_map)

    # Option 2: Include the current word
    word = given_words[index]
    flag = True
    current_word_score = 0

    # Check if the current word can be formed with available characters
    for letter in word:
        if char_map.get(letter, 0) <= 0:
            flag = False
        char_map[letter] = char_map.get(letter, 0) - 1
        current_word_score += words_arr[ord(letter) - 97]

    score_yes = 0

    if flag:
        # Calculate the score if the word is included
        score_yes = current_word_score + max_score_of_words(given_words, index + 1, score, char_map)

    # Restore char_map to its original state (backtrack)
    for letter in word:
        char_map[letter] = char_map.get(letter, 0) + 1

    # Return the maximum score from either including or skipping the word
    return max(score_no, score_yes)


given_words = ['dog', 'cat', 'dad', 'good']

char_map = {
    'a': 1,
    'b': 1,
    'c': 1,
    'd': 3,
    'g': 1,
    'o': 2
}

words_arr = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(max_score_of_words(given_words, 0, 0, char_map))