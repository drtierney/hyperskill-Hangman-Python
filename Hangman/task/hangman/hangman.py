def welcome():
    print("H A N G M A N")
    print("The game will be available soon.")


def play_game():
    word = "python"
    print("Guess the word:")
    guess = input()

    print("You survived!") if guess == word else print("You lost!")


welcome()
play_game()
