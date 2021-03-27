import random


def play_game(words, lives):
    print("H A N G M A N")
    word = random.choice(words)
    dashed = len(word) * "-".split()
    letters = set(word)

    while lives > 0:
        print()
        print("".join(dashed))
        guess = input("Input a letter: ")
        if guess in set(dashed):
            print("No improvements")
            lives -= 1
        elif guess in letters:
            indexes = [index for index, letter in enumerate(word) if letter == guess]
            for i in indexes:
                dashed[i] = guess
            if set(word) == set(dashed):
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            lives -= 1
    else:
        print("You lost!")


play_game(['python', 'java', 'kotlin', 'javascript'], 8)
