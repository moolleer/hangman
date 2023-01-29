import random
import words


def welcome():
    """
    Welcome user and ask if they want to see game instructions
    """

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
        "Before we start, do you want to have a look at the game instructions, y/n ?\n")
    # Make sure user type correct input
    while show_instructions != "y" and show_instructions != "n":
        show_instructions = input(
            "Invalid input, please type y to see the instructions or n to start the game.\n")
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
    # Make sure user type correct input
    while ready != "y" and ready != "n":
        ready = input("Invalid input, please type y or n:\n")
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
        new_letter = input(f"You typed invalid letter: {letter}, pls try again!\n")
        letter = new_letter
    
    tries = 0
    level = ""
    # Generate the word from the wordlist easy, medium or hard and tries
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


def game_run():
    """
    """
    print("Lets play! Good Luck :)")
    print("========================================================")
    # Ask the user to choose difficulty level
    new_word = input("Please enter your prefered difficulty level, e, m or h.\n")
    # Unpack the tuple returned
    word, tries, level = get_word(new_word)
    # Print information to the user
    print(f"You chose to play level {level}. You will have {tries} tries to guess the word!\n")

    print("The word contains: ", len(word), "letters")
    # Prints a hint of number of letters in the word
    print(len(word) * "_ ")
    # List of what the user has guessed
    letters_guessed = []
    #for the letters in the word
    guesses = False
    

    while tries > 0 and guesses == False:
        print(f"You have {tries} left")
        print(f"You have guessed the letters: {letters_guessed}")
        print("---------------------------------------------------")
        user_guess = input("Please enter a letter that you guess is in the word:\n").lower()
        #If the user typed valid input
        if len(user_guess) == 1 and user_guess.isalpha():
            # If user already guessed same letter
            if user_guess in letters_guessed:
                print(f"You have already guessed letter {user_guess}.")
            # If user guessed wrong letter
            elif user_guess not in word:
                print(f"{user_guess} is not in the word, try again!")
                letters_guessed.append(user_guess)
                tries -= 1
            # If user guessed a letter in the word
            else:
                print("You guessed a correct letter!")
                letters_guessed.append(user_guess)
                
        word_hint = ""
        if guesses == False:
            for letter in word:
                if letter in letters_guessed:
                    word_hint += letter
                else:
                    word_hint += "_ "
            print(word_hint)








welcome()

