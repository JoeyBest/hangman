# Hangman

## Table of contents:
| Syntax | Description |
| ----------- | ----------- |
| 1 | Table of Contents|
| 2 | What is the Project? |
| 3 | Aims |
| 4 | Installation instructions |
| 5 | Usage instructions |
| 6 | File structure of the project |
| 7 | License information |


## What is the project?
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Aim of the project:
#### This project is aiming to: 
- Produce python code that can generate a random word
- Accept input guesses from the user
- Navigate these guesses of the word, within the given 5 lives
- Add the correct letters guessed to the word_guessed list
- Decrease the no. of lives for every incorrect guess
- Demonstrate an understanding of all skills used in the project
- Produce a working game which a user and interact with

## What I learned
  #### I have learnt how to use abstraction and encapulation in order to keep my code looking as clean and understanable as possible
  #### I have also learnt how to effectively use a class and to remember to use self. before an attribute when it is in use

  #### Using Docstrings throughout the project allows others and yourself to easily read what is going on in lines of code as well as understand how it works

## Installation instructions:
#### The installation of this project for other users can be done via Git/GitHub
1. First use your terminal / command line and direct it to where you would like the repository (repo) to be
2. On GitHub copy the http:// link ready for us to clone the repo
3. In your terminal/command line use "git clone" followed by the previously copied http:// link
#### This will create a copy of the hangman repository to your local device ready to use

## Usage instructions:
#### When the play_game(word_list) function is run, you will be prompted to enter/guess a letter.

#### The user must enter a charatcter that meets the requirements:
  - Is a singular character
  - Is a letter

#### Following this if their entry met the requirements the message "Good guess! {users_guess} is in the word." will appear. 
#### If the user guess diesn't meet reqirements they'll be prompted "Sorry, {user_guess} is not in the word."
#### However, regardless on the entry, they will be prompted to enter another letter.

## File structure of the project:
  #### this file is structured into sections of relevance and code readbility. For example within the class Hangman, the methods are separated based on what they do.
  - The first being check_guess
  - The second being ask_for_input
#### Within Each of these section, they contain code that is relavent to their purpose. E.g. check_guess only contains code to check if the users guess is in the randomly generated word and other code related to that function.

#### After this is the play_game() function. Each of these parts have been separated for readability purposes. But the play_game() function is left till last as it is the part of the code that uses all the previously mentioned methods. Therefore, it has to be last to be able to access their codes.
  
## License information:



