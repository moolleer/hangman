# Hangman

Hangman is a classic wordgame, usually played by two or more players. The game involves guessing letters in a word whose letters are initially completely hidden, but which are shown as clues when the player successfully guesses them.
The secret word is displayed as horizontal bars as the number of letters in the word, and the player have a number of guesses to find the hidden word. If the user guesses a letter that is not in the word, a line is drawn to a figure which, when completed, will represent a hanged lineman, and then the game is over. 
This Hangman game is written in Python and the user plays in a terminal based window. 

![Responsive Mockup](docs/README-images/amiresponsive.png)

### [View the live website here](https://mooller-hangman.herokuapp.com/)

## Structure

![Flowchart](/docs/README-images/flowchart.PNG)

In the planning process for the game I made a flowchart to identify the essential steps, and to get a visual view over the required steps and the sequential order. I wanted the game to have different levels, and to do this I chose to have three different options for the user, easy, medium and hard. The words vary in difficulty depending on which level the user wants to play, and the number of guesses decreases. I decided to have a words.py file, with three lists that then the target word is randomly selected from. There are about 370 pcs in the easy and medium lists, wich I found on [Github](https://github.com/Xethron/Hangman/blob/master/words.txt) and made some small adjustments to. There are about 200 pcs of hard words, and I found them here [Hangman words](https://www.hangmanwords.com/words).

### Color scheme

To provide a better user experience, I decided to use colors throughout the game. I wanted to have a general color instead of the white standard text, and decided a lighter blue that gives a good contrast against the black background. If the user input some invalid character or letter, this would be shown with a red text to get the users attention. The user should also pay attention to wrong guesses, if the letter already been used or to see with letters have been previously guessed. To this I decided to use a bright orange. For correct guesses or when the word was revealed a light green color was chosen. To stand ut when the user is out of tries, I choose a bright yellow color.

 - General text, blue (\u001b[1;36m)
 - Error messages, red (\u001b[1;31m)
 - Letter not in word, used letters and previously guessed letters, orange (\033[38;2;255;165;0m)
 - Correct guess or when word is found, green (\u001b[1;92m)
 - User is out of tries, yellow (\u001b[1;93m)

## Features

### Existing Features

Welcome page 
- The first page shows a graphic Hangman text and a welcome message to the user. There is also a question if the user would like to see the game instructions before starting the game. I used an online ASCII art generator for the "Hangman" text. 

![Welcome page](/docs/README-images/start.PNG)

Game instructions
- The instructions explains the game and the different levels, then ask if the user is ready to play by typing y or n. 

![Instructions](/docs/README-images/intructions.PNG)

The Game
- The game starts by asking the user what difficulty level they would like to play. The user then choose e for easy, m for medium or h for hard. 

![Choose level](/docs/README-images/startscreen-n.PNG)

- After the user typed in a choice, a message informs about which level the user chose, how many tries the user have, shows how many letters the word contains, and gives a hint with underscores. 
Finally the user is asked to type in a letter that they would like to guess is in the word.

![Chosen level](/docs/README-images/easy-choice.PNG)

- If the user guesses a correct letter that is in the hidden word, a green text will tell the user that the letter is correct. The letter will also be displayed instead of an underscore, at the right place in the word. A message tells the user how many tries that is left, and the letter they guessed is shown in orange. Then the user again is asked to enter another letter.

![Correct guess](/docs/README-images/guess-correct.PNG)

- If the letter is not in the hidden word, the user gets a message that the guess was wrong and a guess is taken of numbers of tries left. 

![Letter not in word](/docs/README-images/not-in-word.PNG)

### Future Features

## Testing

All testing information can be found here [testing.md](https://github.com/moolleer/hangman/blob/main/docs/testing.md)

## Deployment

This application has been deployed by using the Heroku cloud platform and Code Institutes mock terminal for Heroku.
- Steps for deployment:
  - On Heroku dashboard click "create a new app".
  - Assign a unique name to your application. 
  - Choose a region, EU or USA.
  - Select "create app".
  - Navigate to "settings" at the top of the page.
  - If there is any sensitive data that are kept in the gitignore file, you need to allow Heroku access to it by creating a config var. Provide a key in capital letters, example: CREDS, and then add the content of that "CREDS"-file into the value area. 
  - Add another config var with key: PORT, and value of 8000. Then select add.
  - Select "add buildpack".
  - Click python first.
  - Repeat again but this time click nodejs.
  - The order is important, so make sure you select python first and nodejs second. If not you can drag and drop them in the correct order. 
  - Go back up on top of the page and select "deploy". 
  - Choose deployment method. I choose Github. 
  - Then search for your repository name and connect it.    
  - Then you have two options:
     - The first option, enable automatic deployment, which means that Heroku will rebuild the app every time a change is pushed to github.
     - The other option, manually deploy, is the choice I made. 
  - When the project has been deployed, a view button will show with a link to the running app. 

## Credits & Content

- Hangman text is taken from [Text to ASCII Art Generator](http://patorjk.com/software/taag/#p=testall&f=Star%20Wars&t=Hangman)
- Inspiration for how to create a hangman game is taken from [Aminah](https://mardiyyah.medium.com/a-simple-hangman-learnpythonthroughprojects-series-10-fedda58741b), [Youtube](https://www.youtube.com/watch?v=cJJTnI22IF8) and [Invent with Python](https://inventwithpython.com/invent4thed/chapter8.html).
- How to use ANSI escape codes for color [Lihaoyi](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html).



### Media