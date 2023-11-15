import random

class Hangman():
    def __init__(self, word_list = ['kiwi', 'strawberry', 'orange', 'lemon', 'apple'], num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letter = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = [ ]

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

    def ask_for_input(self):
        while True:
            guess = input(('Guess a letter... '))
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

my_hangman = Hangman()
my_hangman.ask_for_input()