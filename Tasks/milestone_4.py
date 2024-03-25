import random

class Hangman():
    def __init__(self, word_list = ['kiwi', 'strawberry', 'orange', 'lemon', 'apple'], num_lives = 5):
        '''Initalising the class parameters: self, world_list and num_lives with a default of 5'''
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letter = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [ ]
        '''Attrubutes of the class are added, self.word generating a randomly chosen word from word_list, 
            word_guessed itertes through the letter in the word and creates a list using '_' for each letter in the word
            num_letter finds the unique number of letters in the word, num_lives uses the default of 5,
            word_list uses the default list in initalisation and list_of_guesses makes an empty list ready for future guesses to be added.
            '''

    def check_guess(self, guess):
        '''Using self and guess as parameters for use within this method to check the users guess'''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            '''the users guess is converted into a lowercase string
                then an if statement is used to print a message only if the guess is in the randomly generated word'''
            for letter in range(len(self.word)):
                if guess == self.word[letter]:
                    self.word_guessed[letter]= guess
            self.num_letter -= 1
            print(self.word_guessed)
            '''This for loop is used to itterate through the letters of the word to be guessed
                and if the users guess is the same as a letter in the word, 
                the letter is added to the word_guessed in the correct '_' position the letter comes from.
                Outside of the loop the number of letters left in the word is reduced by 1, each time a correct letter is guessed'''
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
            '''If the user guess is wrong, the number of lives left is reduced by one,
                in turn a message is printed to say the guess was incorrect
                and returns a message of the number of lives left too'''

    def ask_for_input(self):
        while True:
            '''This while loop continues to loop through the function whilst the result remains True'''
            guess = input(('Guess a letter... '))
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                '''Here the user adds their guess which is then put through the if statement conditions.
                    if the guess is not the length of 1 character or is anything but a letter, it will print an invalid letter message'''
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
                '''if the user makes a guess that has already been added to the list_of_guesses list,
                    it will print a message to notify the user of such.'''
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                '''Here the guess is run through the previous method check_guess
                    and any guesses made are added to the list_of_guesses'''

my_hangman = Hangman()
'''Class is made into an oobject in order to be used/called later'''
my_hangman.ask_for_input()
# Class and method called!