import random

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

def print_answers(guesses):
        for i in range(len(guesses)):
            for j in range(5):
                print(guesses[i][j], end="\s")
            print("\n")

def play_round(guesss, answer, lives):
    letters = []
    guess = guesss.lower()
    for i in range(5):
        letters.append(check_letter(guess[i], i, answer))
    for j in range(5):
        print(letters[j] + '\s')
    if guess == answer:
        return True, lives, letters
    else:
        lives += 1
        return False, lives, letters
    


def main():
    valid_words, available_words = create_data("sgb-words.txt")
    prev_guesses = []
    lives = 0
    print("WELCOME TO WORDLE")
    answer = available_words[random.randrange(0, len(available_words))]
    while True:
        checked = []
        status = None
        print("\n")
        guess = input("Put your guess here, no spaces please! : ").split()
        print("\n")
        if guess in valid_words:
            end_round = play_round(guess, answer, lives)
            if end_round[0] == True:
                print("Congrats! You win! you had " + str(GUESSES - lives) + " lives left, good job!")
                break
            elif end_round[0] == False:
                

            
        else:
            print("Thats not a valid word, try again!")
            continue
        

