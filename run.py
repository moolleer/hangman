"""
A Hangman game
"""
import random
import words


def welcome():
    """
    Welcome user and ask if they want to see game instructions
    """
    print("================================================\n")
    print("\u001b[1;36m")
    print(" _")
    print("| |")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |")
    print("                   |___/\u001b[0m")
    print("\n")
    print("================================================\n")
    print("\u001b[1;36mWelcome to play Hangman!!!\u001b[0m")
    print("================================================\n")

    # Make sure user can see game instructions
    show_instructions = input(
        "\u001b[1;36mBefore we start, do you want to have"
        " a look at the game instructions, y/n ?\u001b[0m\n"
    )
    print("\n")
    # Make sure user type correct input
    while show_instructions != "y" and show_instructions != "n":
        show_instructions = input(
            "\u001b[1;31mInvalid input, please type y to see the instructions"
            " or n to start the game.\u001b[0m\n"
        )
        print("---------------------------------------------------")
    # Show instructions or start game
    if show_instructions == "y":
        game_intructions()
    elif show_instructions == "n":
        game_run()


def game_intructions():
    """
    Show game instructions and ask user if they are ready to play.
    Runs game or go back to welcome page
    """
    print(
        "=============================================="
        "================================"
    )
    print(
        "\u001b[1;36mHow to play Hangman!\n"
        "Hangman is a simple word guessing game.\n"
        "You try to figure out an unknown word by guessing letters.\n"
        "If you guess the right letter that is within the word,\n"
        "the letter appears at its correct position.\n"
        "If you guess to many letters, which do not appear in the word,\n"
        "you lose and the game is over.\n"
    )
    print(
        "You can choose between three different levels:\n"
        "Easy: You have 10 guesses to find the right word.\n"
        "The words are shorter and common.\n"
        "Medium: You have 8 guesses to find the right word."
        "The words could be longer and less common.\n"
        "Hard: You have 6 guesses to find the right word."
        "The words are both short\n and long, and could be uncommon."
        "\u001b[0m"
    )

    print(
        "=============================================="
        "================================"
    )

    ready = input("\u001b[1;36mNow, are you ready to play y/n ?\u001b[0m\n")
    print("\n")
    # Make sure user type correct input
    while ready != "y" and ready != "n":
        ready = input(
            "\u001b[1;31mInvalid input,"
            "please type y or n:\u001b[0m\n"
        )
        print("----------------------------------------")
        print("\n")
    # Run game or get back to welcome page
    if ready == "y":
        game_run()
    else:
        welcome()


def get_word(letter):
    """
    Checks if user entered correct letter e, m or h.
    Get a randomized word from the words module, depending on the chosen level
    easy, medium or hard.
    Adds number of tries and level depending on user choice.
    """
    # Make sure the user types the correct input.
    while letter != "e" and letter != "m" and letter != "h":
        new_letter = input(
            f"\u001b[1;31mYou typed invalid letter: {letter},"
            " pls try again, e for easy, m for medium\n"
            " or h for hard!\u001b[0m\n"
        )
        print("---------------------------------------------------")
        letter = new_letter

    tries = 0
    level = ""
    # Generate the word from the wordlist easy, medium or hard
    # and add number of tries.
    # Returns the difficulty level
    if letter == "e":
        e_word = random.choice(words.EASY_WORDS)
        tries = 10
        level = "easy"
        return e_word, tries, level
    elif letter == "m":
        m_word = random.choice(words.MEDIUM_WORDS)
        tries = 8
        level = "medium"
        return m_word, tries, level
    elif letter == "h":
        h_word = random.choice(words.HARD_WORDS)
        tries = 6
        level = "hard"
        return h_word, tries, level


def play_again():
    """
    Ask user if they want to play again.
    Restart the game or go back to welcome page.
    """
    play_game_again = input(
        "\u001b[1;36mWould you like to play again?\n"
        "Type y/n.\u001b[0m\n"
    )
    # Make sure user type correct input
    while play_game_again != "y" and play_game_again != "n":
        play_game_again = input(
            "\u001b[1;31mInvalid input,"
            "type y for yes and n for no\u001b[0m\n"
        )

    if play_game_again == "y":
        game_run()
    else:
        print("----------------------------------------")
        print(
            "\u001b[1;36mThank you for playing hangman!!\n"
            "If you still want to play"
            " just click the run program button:)\u001b[0m"
        )


def game_run():
    """
    Main function of the game. Loops and check if user input matches the
    secret word and compare results.
    """
    print("\u001b[1;36mLets play! Good Luck :)\u001b[0m")
    print("========================================================")
    # Ask the user to choose difficulty level
    new_word = input(
        "\u001b[1;36mPlease enter your prefered difficulty level,"
        " e, m or h.\n"
    )
    # Unpack the tuple returned
    word, tries, level = get_word(new_word)
    tries_start = tries
    # Print information to the user
    print(
        f"\u001b[1;36mYou chose to play level {level}. You will have {tries}"
        " tries to guess the word!\n")
    print("The word contains:", len(word), "letters\u001b[0m")
    # Prints a hint of number of letters in the word
    print(len(word) * "_ ")
    print("\n")
    # List of what the user has guessed
    letters_guessed = []
    # For the letters in the word
    guesses = set(word)
    # Checks if user have tries left.
    # Checks if letters are still in the word.
    while tries > 0 and len(guesses) > 0:
        print(f"\u001b[1;36mYou have {tries} tries left.")
        # Prints the letters user have guessed.
        print(
            "You have guessed the letters: "
            f"\033[38;2;255;165;0m{', '.join(letters_guessed)}"
            "\u001b[0m"
        )
        print("---------------------------------------------------")
        user_guess = input(
            "\u001b[1;36mPlease enter a letter that you"
            " guess is in the word:\n\u001b[0m").lower()
        # If the user typed valid input
        if len(user_guess) == 1 and user_guess.isalpha():
            # If user already guessed same letter
            if user_guess in letters_guessed:
                print(
                    "\033[38;2;255;165;0mYou have already guessed "
                    f"letter {user_guess}.\u001b[0m\n"
                )
                print("---------------------------------------------------")
            # If user guessed wrong letter
            elif user_guess not in word:
                print(
                    f"\033[38;2;255;165;0m{user_guess} is not in the word,"
                    " try again!\n\u001b[0m"
                )
                letters_guessed.append(user_guess)
                tries -= 1
                print("---------------------------------------------------")
            # If user guessed a letter in the target word
            else:
                print("\u001b[1;92mYou guessed a correct letter!\u001b[0m\n")
                letters_guessed.append(user_guess)
                guesses.remove(user_guess)
                print("---------------------------------------------------")
        else:
            print("\u001b[1;31mInvalid input, letters only please!\u001b[0m\n")
            print("-------------------------------------------------------")
        # Show the correct letters in the target word at the correct place,
        # otherwise show underscores.
        word_hint = ""
        if len(guesses) > 0:
            for letter in word:
                if letter in letters_guessed:
                    word_hint += letter
                else:
                    word_hint += "_ "
            print(word_hint)
            print("\n")

    if tries == 0:
        # if the user runs out of guesses
        print("\u001b[1;93mOops, sorry you ran out of tries! :(")
        # Show the hidden word to the user
        print(f"The word was:\u001b[0m {word}")
        # Display the hangman picture
        print(HANGMANPIC)
        print("---------------------------------------------------")
        play_again()

    else:
        # If the user guessed the word right, show message and how many tries
        tries_left = tries_start - tries
        print(
            "\u001b[1;92m*** Congratulations, you win!! ***\nYou guessed the"
            f" correct word: {word}"
        )
        print(f"     You did it in {tries_left} tries.")
        print("          Well done!\u001b[0m")
        print("---------------------------------------------------")
        play_again()


HANGMANPIC = '''\u001b[1;31m
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\u001b[0m'''

welcome()
