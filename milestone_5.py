import random
from milestone_2 import word_list
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters_unguessed = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters_unguessed -= 1 
        else:
            self.num_lives -= 1 
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if guess == "!":
                return "restart"
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)
                break
        return ""
    def board(self):
        print(self.word_guessed)
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        game.board()
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters_unguessed > 0:
            command = game.ask_for_input()
            if command == "restart": 
                play_game(word_list)
                break
        else:
            print("Congratulations. You won the game!")
            break
play_game(word_list)