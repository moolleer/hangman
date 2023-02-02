## Testing

### Manual Testing

1. Asking user if they want to see game instructions?
   - The game instructions are expected when user enters y. 
   - The game is expected to start if the user enters n.
   - Invalid input message in red is expected if user enters anything else but y or n.

Enter y shows the instructions as expected.

![Instructions y](/docs/README-images/instructions-y.png)

Enter n starts the game as expected.

![Instructions n](/docs/README-images/instructions-no.png)

Tested to enter j, and then 3. An invalid input gives an error message in red as expected. When y is entered the instructions shows.

![Instructions invalid](/docs/README-images/instructions-invalid.png)

2. After reading game instructions, ask user if they are ready to play?
     - The game is expected to start when user enters y.
     - The user is expected to be directed back to welcome message when they enter n.
     - Invalid input message in red is expected if user enters anything else but y or n.

Enter y and the game starts as expected.

![Instructions start game](/docs/README-images/instructions-play.png)

When n is entered the user gets redirected back to welcome message as expected.

Tested to enter j, and then 3. An invalid input gives an error message in red as expected. When y is entered the game starts.

![Instructions invalid](/docs/README-images/instructions-invalid-play.png)

3. Ask user to choose difficulty level
      - The user get a message of choosen difficulty level and numbers of tries. The hidden word is displayed by how many letters that is in the word and shown with underscores as an hint is expected when user enter e, m, or h. 
      - Number of tries and the letters guessed is also expected when user enter e, m or h.
      - Invalid input message in red is expected if user enters anything else but y or n.

The message, level and number of tries works as expected.

![Levels](/docs/README-images/choose-level.png)

Tested to enter j, and then 3. An invalid input gives an error message in red as expected. When e, m or h is entered the game starts.

![Levels](/docs/README-images/chosen-level.png)

4. Ask user to guess word
      - Checks if user guess is in the hidden word and display feedback to user is expected when letter is entered.
      - If letter is not in the hidden word, an orange text message is expected.
      - If letter have been guessed before an orange text message is expected.
      - If letter is in word, a green message and the letter placed at the correct position instead of an underscore is expected.
      - The letters guessed added to a list is expected.
      - Invalid input message in red is expected if user enters anything else than a letter.

Check user guess and show message in orange for letter not in word works as expected.

![Guess](/docs/README-images/guess-word-not-in-word.png)

If user guess the same letter as already been guessed a orange message tells this to the user works as expexted.

![Already guessed](/docs/README-images/guessed-letter.png)

When the user guess a letter that is in the word, a green message tells this to the user and the letter is placed at the correct position instead of an underscore. The guessed letters is also added to the list (marked in red) as expected.

![Letter in word](/docs/README-images/letter-is-inword.png)

If the user enter anything but a letter a invalid input message in red shows as expected.

![Invalid](/docs/README-images/guess-invalid-char.PNG)

5. Out of tries
     - If user runs out of tries a yellow message that reveals the hidden word in white color is expected.

The message and reveal of the hidden word works as expected.

![Game over](/docs/README-images/game-over.PNG)

6. Correct word
    - If the user guesses the word right, a congratulations message in green is expected.

The correct word message is shown as expecting.

![Correct word](/docs/README-images/correct-word.PNG)


7. Play again
     - When the user have run out of tries or found the hidden word, a message that ask if they wan't to play again or not is expected.
     - If the user chose to play again the game starts over and ask user to enter a letter is expected.
     - If the user don't want to play again a farewell message is expected.
     - Invalid input message in red is expected if user enters anything else but y or n.

The play again message works as expected.

![Play again](/docs/README-images/play-again.png)

The thank you for playing message works as expected. 

![End game](/docs/README-images/play-again-no.PNG)

The invalid input message works as expected.

![Invalid](/docs/README-images/play-again-invalid-input.PNG)

### Code Validation
Python code was validated by Code Institutes [Python Linter](https://pep8ci.herokuapp.com/) and no errors where found.

![Python validation](/docs/README-images/python-linter.PNG)

![Python validation words](/docs/README-images/words.py.png)

### Bugs and fixes