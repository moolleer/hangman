import random
import words


def get_word(letter):
    """
    Checks if user entered correct letter e, m or h.
    Get a randomized word from the word module, depending on the chosen level
    easy, medium or hard.
    """
    while letter != "e" and letter != "m" and letter != "h":
        new_letter = input(f"You typed invalid letter: {letter}, pls try again!\n")
        letter = new_letter

    if letter == "e":
        e_word = random.choice(words.EASY_WORDS)
        print(e_word)
        return e_word
    elif letter == "m":
        m_word = random.choice(words.MEDIUM_WORDS)
        print(m_word)
        return m_word
    elif letter == "h":
        h_word = random.choice(words.HARD_WORDS)
        print(h_word)
        return h_word

  
get_word("ö")
