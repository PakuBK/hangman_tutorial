import random

hangman_figure = {
    0 : " _____\n"
        " |   |\n"
        " |    \n"
        " |    \n"
        " |    \n"
        " A    \n",
    1 : " _____\n"
        " |   |\n"
        " |   O\n"
        " |    \n"
        " |    \n"
        " A    \n",
    2 : " _____\n"
        " |   |\n"
        " |   O\n"
        " |   |\n"
        " |    \n"
        " A    \n",
    3 : " _____\n"
        " |   |\n"
        " |   O\n"
        " |  /|\n"
        " |    \n"
        " A    \n",
    4 : " _____\n"
        " |   |\n"
        " |   O\n"
        " |  /|\ \n"
        " |    \n"
        " A    \n",
    5: " _____\n"
       " |   |\n"
       " |   O\n"
       " |  /|\ \n"
       " |  /\n"
       " A    \n",
    6: " _____\n"
       " |   |\n"
       " |   O\n"
       " |  /|\ \n"
       " |  / \ \n"
       " A    \n",
}


def load_words():
    with open("words.txt", "r") as file:
        for line in file:
            return line.split(",")


def get_blank(word, guesses):
    """ Calculates the blank word """
    blank = ["_" for i in range(0,len(word))]
    for guess in guesses:
        for i,char in enumerate(word):
            if char == guess:
                blank[i] = char
    return blank


def get_random_word(words):
    return random.choice(words)


def get_guess():
    while True:
        guess = input("guess:")
        if len(guess) > 1:
            print("Illegal guess. Try again.")
        else:
            return guess


def print_pretty_blank(blank):
    str_blank = ""
    for ele in blank:
        str_blank += ele+" "
    print(str_blank)


def start(words):
    mistakes = 0

    word = get_random_word(words)
    guessed_letters = []
    blank_word = get_blank(word=word, guesses=guessed_letters)

    print(hangman_figure[mistakes])
    print_pretty_blank(blank_word)

    while True:
        guess = get_guess()
        guessed_letters.append(guess)
        blank_word = get_blank(word=word, guesses=guessed_letters)

        if guess in word:
            print("Nice!")

        else:
            mistakes += 1
            print(f"Wrong! : Mistakes {mistakes}")

        if "_" not in blank_word:  # win Condition
            print(f"You won! \nThe word was '{word}' ")
            break
        elif mistakes >= 6:
            print(hangman_figure[mistakes])
            print(f"You lose! \nThe word was '{word}'")
            break
        else:
            print(hangman_figure[mistakes])
            print_pretty_blank(blank_word)


if __name__ == "__main__":
    words = load_words()  # words.txt separated by commas
    start(words=words)  # start game
