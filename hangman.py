import random

# A simple hangman game for the Rigetti Computing internship candidacy
# Written by Aaron Vontell
# October 19th, 2016

# Representation of a simple Hangman game, with methods
# for guessing letters and determining the end of the game
class Hangman:
    
    # Creates a Hangman game. If a word is given, use that word for the game;
    # otherwise, use a random word from the built-in word list. The Hangman 
    # game can also override the number of lives for the player (default is 6)
    def __init__(self, word=None, lives=6):
        
        # Define the word
        if word is None:
            default_words = ["rigetti", "quantum", "physics", "computing", "internship"]
            self.word = default_words[int(random.random() * len(default_words))]
        else:
            self.word = word
            
        # Instantiate lists and vars that will hold guessed
        # letters, lives left, and the progress of the word
        self.guessed = []
        self.presented = ["_"] * len(self.word)
        self.lives = lives
        
    # Guess a letter in the word; returns the number of found
    # letters in the game word. Returns -1 if that letter has
    # already been guessed.
    def guess_letter(self, letter):
        
        if letter in self.guessed:
            return -1
        
        occurrences = [i for i in range(len(self.word)) if self.word[i] == letter]
            
        # If the letter is not in the word, retract 1 life
        if len(occurrences) == 0:
            self.lives -= 1
            
        # Update the presented word
        for i in occurrences:
            self.presented[i] = letter
            
        self.guessed.append(letter)
        return len(occurrences)
    
    # Returns True if the game is over (lives is 0, or word is guessed)
    def is_over(self):
        return self.lives <= 0 or "".join(self.presented) == self.word
    
    # Returns the current word progress
    def get_presented(self):
        return " ".join(self.presented)
    
    # Returns the number of lives of the player
    def get_lives(self):
        return self.lives
    
    # Returns the list of guessed characters
    def get_guessed(self):
        return self.guessed
        

# Script that provides the prompts for the game
def start_game():
    
    print("Welcome to Hangman!")
    word = input("What word do you want to play with (or blank for a random word)? ")
    lives = input("How many lives to start with (or blank for 6)? ")
    
    word = None if word == "" else word
    lives = 6 if not lives.isdigit() else int(lives)
    
    game = Hangman(word, lives)
    
    while not game.is_over():
        print("")
        print(game.get_presented())
        print("Guessed letters: " + " ".join(game.get_guessed()))
        print("Lives left: " + str(game.get_lives()))
        guess = input("Guess a letter: ")
        
        result = game.guess_letter(guess)
        if result == -1:
            print("You already guessed this letter!")
    else:
        
        if game.get_lives() == 0:
            print("You lost! The word was '" + game.word + "'")
        else:
            print("Congrats! You guessed the word, '" + game.word + "'")
    
start_game()