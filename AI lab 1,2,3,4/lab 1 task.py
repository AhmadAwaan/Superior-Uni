import random

def hangman(word):
    guessed = '_' * len(word)
    attempts = 6
    while attempts > 0 and '_' in guessed:
        print("Current word:", guessed)
        guess = input("Guess a letter: ").lower()
        if guess in word:
            guessed = ''.join([letter if letter == guess or letter in guessed else '_' for letter in word])
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)
    if '_' not in guessed:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Game over! The word was:", word)

word_list = ['python', 'hangman', 'programming']
hangman(random.choice(word_list))