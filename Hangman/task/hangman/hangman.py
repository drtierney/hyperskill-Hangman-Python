import random


def welcome():
    print("H A N G M A N")


def choose_word(words):
    return random.choice(words)


def start_game(words):
    word = choose_word(words)
    guess = input("Guess the word: ")

    print("You survived!") if guess == word else print("You lost!")


languages = ['python', 'java', 'kotlin', 'javascript']
welcome()
start_game(languages)
