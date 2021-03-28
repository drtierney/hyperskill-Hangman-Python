import random
from string import ascii_lowercase


def play_game(words, lives):
    print("H A N G M A N")
    word = random.choice(words)
    dashed = len(word) * "-".split()
    letters = set(word)
    guesses = set()

    while lives > 0:
        print()
        print("".join(dashed))
        guess = input("Input a letter: ")
        if guess in guesses:
            print("You've already guessed this letter")
        elif len(guess) != 1:
            print("You should input a single letter")
        elif guess not in ascii_lowercase:
            print("Please enter a lowercase English letter")
        elif guess in letters:
            guesses.add(guess)
            indexes = [index for index, letter in enumerate(word) if letter == guess]
            for i in indexes:
                dashed[i] = guess
            if set(word) == set(dashed):
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            guesses.add(guess)
            print("That letter doesn't appear in the word")
            lives -= 1
    else:
        print("You lost!")


print('Type "play" to play the game, "exit" to quit:')
choice = input()
if choice == "play":
    play_game(['python', 'java', 'kotlin', 'javascript'], 8)
elif choice == "exit":
    exit()
