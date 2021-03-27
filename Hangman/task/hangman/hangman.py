import random


def play_game(words):
    print("H A N G M A N")
    print()

    word = random.choice(words)
    dashed = len(word) * "-".split()
    letters = set(word)
    print("".join(dashed))

    for _ in range(8):
        guess = input("Input a letter: ")
        if guess in letters:
            indexes = [index for index, letter in enumerate(word) if letter == guess]
            for i in indexes:
                dashed[i] = guess
        else:
            print("That letter doesn't appear in the word")
        print()
        print("".join(dashed))


play_game(['python', 'java', 'kotlin', 'javascript'])
print("Thanks for playing!")
print("We'll see how well you did in the next stage")
