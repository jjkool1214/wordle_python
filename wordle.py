import random
import re

GUESSES = 6

def create_data(filename):
    full_set = set()
    full_list = list()
    with open(filename) as file:
        for line in file:
            full_set.add(line.strip())
            full_list.append(line.strip())
    return full_set, full_list

def check_letter(letter, place, word, dupe):
        if letter != dupe:
            for i in range(5):    
                if letter == word[i]:
                    if place == i:
                        return "\033[1;32;40m " + letter + " "
                    return "\033[1;33;40m " + letter + " "
            return "\033[1;30;40m " + letter + " "
        elif letter == dupe:
            places = set()
            for i in range(5):
                if letter == word[i]:
                    places.add(i)
            if place in places:
                return "\033[1;32;40m " + letter + " "
            else:
                return "\033[1;33;40m " + letter + " "


def check_dupes(word):
    for i in range(5):
        letter = word[i]
        count = 0
        for j in range(5):
            if letter == word[j]:
                count += 1
        if count > 1:
            return word[i]
    return None

def print_answers(guesses):
        for i in range(len(guesses)):
            for j in range(5):
                print(guesses[i][j], end=" ")
            print("\n")

def play_round(guess, answer, lives):
    letters = []
    dupes = check_dupes(answer)
    for i in range(5):
        letters.append(check_letter(guess[i], i, answer, dupes))
    if guess == answer:
        return True, lives, letters
    else:
        lives += 1
        return False, lives, letters
    
def main():
    valid_words, available_words = create_data("sgb-words.txt")
    checked = []
    lives = 0
    print("WELCOME TO WORDLE")
    answer = available_words[random.randrange(0, len(available_words))]
    while True:
        print("\n")
        guess = input("Put your guess here, no spaces please! : ").strip('').lower()
        print("\n")
        if guess in valid_words:
            guessed = re.findall("\w{1}", guess)
            end_round = play_round(guessed, re.findall("\w{1}", answer), lives)
            lives = end_round[1]
            checked.append(end_round[2])
            if end_round[0] == True:
                print("Congrats! You win! you had " + str(GUESSES - lives) + " lives left, good job!")
                print("\n")
                print_answers(checked)
                print("\033[1;37;40m   ")
                break
            elif (end_round[0] == False) and (lives >= GUESSES):
                print("You lost, womp womp, correct answer was " + answer)
                print("\n")
                print_answers(checked)
                print("\033[1;37;40m   ")
                break
            else:
                print_answers(checked)
                print("\033[1;37;40m   ")
        else:
            print("Thats not a valid word, try again!")
            continue
    
main()
