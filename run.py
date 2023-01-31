import random
import words


def welcome():
    """
    Welcome user and ask if they want to see game instructions
    """
    print("================================================\n")
    print(" _")
    print("| |")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |")
    print("                   |___/")

    print("================================================\n")
    print("Welcome to play Hangman!!!")
    print("================================================\n")

    # Make sure user can see game instructions
    show_instructions = input(
        "Before we start, do you want to have"
        " a look at the game instructions, y/n ?\n"
    )
    print("\n")
    # Make sure user type correct input
    while show_instructions != "y" and show_instructions != "n":
        show_instructions = input(
            "\u001b[1;31mInvalid input, please type y to see the instructions"
            " or n to start the game.\u001b[0m\n"
        )
    # Show instructions or start game
    if show_instructions == "y":
        game_intructions()
    elif show_instructions == "n":
        game_run()


def game_intructions():
    """
    Show game instructions and ask user if they are ready to play
    """
    print(
        "How to play Hangman!\n"
        "Hangman is a simple word guessing game.\n"
        "You try to figure out an unknown word by guessing letters.\n"
        "If you guess the right letter that is within the word,"
        "the letter appears at its correct position.\n"
        "If you guess to many letters, which do not appear in the word,"
        "you lose and the game is over.\n"
    )
    print(
        "You can choose between three different levels:\n"
        "Easy: You have 10 guesses to find the right word."
        "The words are shorter and common.\n"
        "Medium: You have 8 guesses to find the right word."
        "The words could be longer and less common.\n"
        "Hard: You have 6 guesses to find the right word."
        "The words are both short and long, and could be uncommon.\n"
    )

    ready = input("Now, are you ready to play y/n ?\n")
    print("\n")
    # Make sure user type correct input
    while ready != "y" and ready != "n":
        ready = input(
            "\u001b[1;31mInvalid input,"
            "please type y or n:\u001b[0m\n"
        )
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
    """
    # Make sure the user types the correct input.
    while letter != "e" and letter != "m" and letter != "h":
        new_letter = input(
            f"\u001b[1;31mYou typed invalid letter: {letter},"
            " pls try again, e for easy, m for medium"
            " or h for hard!\u001b[0m\n"
        )
        letter = new_letter

    tries = 0
    level = ""
    # Generate the word from the wordlist easy, medium or hard
    #  and add number of tries.
    # Also returns the difficulty level
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
    play_game_again = input("Would you like to play again?\n Type y/n.\n")
    # Make sure user type correct input
    while play_game_again != "y" and play_game_again != "n":
        play_game_again = input(
            "\u001b[1;31mInvalid input,"
            "type y for yes and n for no\u001b[0m\n"
        )

    if play_game_again == "y":
        game_run()
    else:
        print(
            "Thank you for playing hangman!!\nIf you still want to play"
            " just click the run program button:)"
        )


def game_run():
    """
    Main function of the game. Check if user input matches the
    secret word and compare results.
    """
    print("Lets play! Good Luck :)")
    print("========================================================")
    # Ask the user to choose difficulty level
    new_word = input(
        "Please enter your prefered difficulty level,"
        " e, m or h.\n"
    )
    # Unpack the tuple returned
    word, tries, level = get_word(new_word)
    tries_start = tries
    # Print information to the user
    print(
        f"You chose to play level {level}. You will have {tries}"
        "tries to guess the word!\n")
    print("The word contains: ", len(word), "letters")
    # Prints a hint of number of letters in the word
    print(len(word) * "_ ")
    print("\n")
    # List of what the user has guessed
    letters_guessed = []
    # For the letters in the word
    guesses = set(word)

    while tries > 0 and len(guesses) > 0:
        print(f"You have {tries} tries left.")
        print(f"You have guessed the letters: {', '.join(letters_guessed)}")
        print("---------------------------------------------------")
        user_guess = input(
            "Please enter a letter that you"
            " guess is in the word:\n").lower()
        # If the user typed valid input
        if len(user_guess) == 1 and user_guess.isalpha():
            # If user already guessed same letter
            if user_guess in letters_guessed:
                print(f"You have already guessed letter {user_guess}.\n")
            # If user guessed wrong letter
            elif user_guess not in word:
                print(f"{user_guess} is not in the word, try again!\n")
                letters_guessed.append(user_guess)
                tries -= 1
            # If user guessed a letter in the word
            else:
                print("You guessed a correct letter!\n")
                letters_guessed.append(user_guess)
                guesses.remove(user_guess)
        else:
            print("\u001b[1;31mInvalid input, letters only please!\u001b[0m\n")
        # Showes the correct letters in the words at right place,
        # or underscores
        word_hint = ""
        if len(guesses) > 0:
            for letter in word:
                if letter in letters_guessed:
                    word_hint += letter
                else:
                    word_hint += "_ "
            print(word_hint)

    if tries == 0:
        # if the user runs out of guesses
        print("Oops, sorry you ran out of tries!")
        # Show the hidden word to the user
        print(f"The word was {word}!")
        print("___________________________________")
        play_again()

    else:
        # If the user guessed the word right
        tries_left = tries_start - tries
        print(
            f"Congratulations, you win!! You guessed the correct word: {word}!"
        )
        print(f"You did it in {tries_left} tries.")
        print("___________________________________")
        play_again()


welcome()
