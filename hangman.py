import random


class Hangman():
    ''' 
    This class is used to create the Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a random word from the word_list and a default number of lives.
    '''

    def __init__(self, word_list = ['kiwi', 'strawberry', 'orange', 'lemon', 'apple'], num_lives = 5):
        '''
        This method is used to initialise this instance of the Hangman class.

        Parameters:
        ----------
        word_list: list
            List of words to be used in the game
        num_lives: int
            Number of lives the player has

        Attributes:
        ---------- 
        word: str
            The randomly chosen word from word_list to be guessed by the user 
        word_guessed: list
            Itertes through the letter in the word and creates a list using '_' for each letter in the word
            E.g. if the word is 'orange', the word_guessed list would be ['_', '_', '_', '_', '_', '_']
            If the user guessed 'o', the list would appear as ['o', '_', '_', '_', '_', '_']
        num_letter: int
            The unique number of letters in the word
        num_lives: int
            The number of lives the user has, from which the default is 5
        word_list: list
            The default list in initalisation 
        list_of_guesses: list
            An empty list ready for future guesses to be added
        '''
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letter = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [ ]


    def check_guess(self, guess):
        '''
        This method is used to check the letter the user has entered.

        The users guess is converted into a lowercase string
        If the letter is in the word, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives in num_lives by 1.
        
        Parameters:
        ----------
        guess: str
            The users letter input that will be checked  
        ''' 
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(self.word)):
                if guess == self.word[letter]:
                    self.word_guessed[letter]= guess
            self.num_letter -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''
        This method is used to ask the user to enter a letter.

        If the guess is not the length of 1 character or is anything but a letter, it will print an invalid letter message.
        Guesses made are added to the list_of_guesses list.
        If the user makes a guess that has already been guessed, it will print a message to notify the user of such.
        '''
        while True:
            guess = input('Guess a letter... ')
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
        # This while loop continues to loop through the function whilst the result remains True.
            # Here the user adds their guess which is then put through the if statement conditions.
            # If the guess is not a single alphabetical character, an invalid letter message is printed.

#my_hangman = Hangman()
#my_hangman.ask_for_input() <- test run of methods

def play_game(word_list):
    num_lives = 5
    game = Hangman()
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letter > 0:
            game.ask_for_input()
        else: 
            num_lives != 0 and game.num_letter == 0
            print('Congratulations. You won the game!')
            break
    # This while loop keeps the game going as until the number of lives = 0 or the word is guessed.
    # If lives = 0, or the word is guessed the according message will appear. 

if __name__ == '__main__':
    word_list = ['kiwi', 'strawberry', 'orange', 'lemon', 'apple']        
    play_game(word_list)
    # This is the code is used to activate the game