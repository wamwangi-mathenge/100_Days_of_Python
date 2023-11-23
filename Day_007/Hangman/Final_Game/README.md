# Hangman Game Project

## Introduction
This is a simple implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list, and the player has to guess the letters in the word before running out of lives.

## Features
- Random word selection from a predefined list.
- Display of the current state of the word with blanks for unguessed letters.
- Feedback for correct and incorrect guesses.
- Visual representation of the hangman as the player makes incorrect guesses.
- Win or lose message at the end of the game.

## Files

- [hangman.py](./hangman.py): The main Python script containing the Hangman game logic.
- [hangman_words.py](./hangman_words.py): A module containing the word list used by the game.
- [hangman_art.py](./hangman_art.py): A module containing ASCII art for the Hangman stages and the game logo.

## How to Run
1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the hangman.py file.
4. Run the command: python hangman.py

## Gameplay
1. At the start of the game, the Hangman logo is displayed.
2. Blanks representing the letters in the word are shown.
3. The player is prompted to guess a letter.
4. The game provides feedback on whether the letter is correct or incorrect.
5. The Hangman stages are displayed based on the number of incorrect guesses.
6. The game continues until the player either guesses the word or runs out of lives

## Customization
- You can modify the word_list in hangman_words.py to include your own words.
- ASCII art in hangman_art.py can be customized or replaced with your own designs.

## Credits
ASCII art was adapted from various sources and modified for this project.

## License
This project is licensed under the MIT License

## Author
Brian Mathenge