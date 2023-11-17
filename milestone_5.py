import random

class Hangman():
    def __init__(self, word_list = ['kiwi', 'strawberry', 'orange', 'lemon', 'apple'], num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letter = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [ ]
        '''Initalising the class parameters: self, world_list and num_lives with a default of 5
        Attrubutes of the class are added, self.word generating a randomly chosen word from word_list, 
        word_guessed itertes through the letter in the word and creates a list using '_' for each letter in the word
        num_letter finds the unique number of letters in the word, num_lives uses the default of 5,
        word_list uses the default list in initalisation and list_of_guesses makes an empty list ready for future guesses to be added.
        '''


    def check_guess(self, guess):
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
            '''Using self and guess as parameters for use within this method to check the users guess
            the users guess is converted into a lowercase string
            then an if statement is used to print a message only if the guess is in the randomly generated word'''
            
            '''The for loop is used to itterate through the letters of the word to be guessed
            and if the users guess is the same as a letter in the word, 
            the letter is added to the word_guessed in the correct '_' position the letter comes from.
            Outside of the loop the number of letters left in the word is reduced by 1, each time a correct letter is guessed'''
            
            '''If the user guess is wrong, the number of lives left is reduced by one,
            in turn a message is printed to say the guess was incorrect
            and returns a message of the number of lives left too'''

    def ask_for_input(self):
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
                '''This while loop continues to loop through the function whilst the result remains True.
                Here the user adds their guess which is then put through the if statement conditions.
                if the guess is not the length of 1 character or is anything but a letter, it will print an invalid letter message'''
                
                '''if the user makes a guess that has already been added to the list_of_guesses list,
                    it will print a message to notify the user of such.'''
                
                '''Here the guess is run through the previous method check_guess
                    and any guesses made are added to the list_of_guesses'''
            


#my_hangman = Hangman()
#my_hangman.ask_for_input() <- test run of methods

word_list = ['kiwi', 'strawberry', 'orange', 'lemon', 'apple']

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
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
            ''' The class is converted into an variable/object (game) with the parameters word_list and num_lives,
            in order to access it's attributes.
            A while loop is created to continuously run through the code until either the user loses all their lives
            (num_lives = 0), or they succesfully manage to guess the correct word. either result will print a message of their outcome.
            the loop is then broken out of
            '''
play_game(word_list)
'''this is the Code used to activate the game'''