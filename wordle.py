import random
import re

GUESSES = 6

def create_data(filename):
    full_set = set()
    full_list = list()
    with filename as file:
        for line in file:
            full_set.add(line.strip())
            full_list.append(line.strip())
    return full_set, full_list

def check_letter(letter, place, word):
    for i in range(5):
        if letter == word[i]:
            if place == i:
                return "\033[1;32;40m " + letter + " "
            return "\033[1;33;40m " + letter + " "
    return "\033[1;30;40m " + letter + " "

def play_round(guess, answer, lives, valid_words, prev_guesses):
    letters = []
    if guess in valid_words:
        for i in range(5):
            letters.append(check_letter(guess[i], i, answer))
        for j in range(5):
            print(letters[j] + '\s')
        if guess == answer:
            print()


def print_guess(lst):
    for letter in lst:
        print(letter)



def main():
    valid_words, available_words = create_data("sgb-words.txt")
    prev_guesses = []