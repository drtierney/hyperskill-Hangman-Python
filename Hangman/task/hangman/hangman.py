import random


def choose_word(choices):
    return random.choice(choices)


def hint_word(word):
    return word[0:3] + ("-" * (len(word) - 3))


def guess_word(guess, word):
    print("You survived!") if guess == word else print("You lost!")


def start_game(words):
    print("H A N G M A N")
    word = choose_word(words)
    hint = hint_word(word)
    guess_word(input(f"Guess the word {hint}: "), word)


start_game(['python', 'java', 'kotlin', 'javascript'])
