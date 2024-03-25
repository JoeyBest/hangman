import random

word_list = ['kiwi', 'strawberry', 'orange', 'lemon', 'apple']
#print(word_list)

word = random.choice(word_list)
#print(word)

guess = input('Enter a single letter... ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess')
else:
    print('Oops, thats not a valid input!')


  