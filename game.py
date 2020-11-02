# Create your Game class logic in here.
import random
from phrase import Phrase

class Game:
    def __init__(self):
        self.phrases = [
            Phrase("swings and roundabouts"),
            Phrase("the ball is mightier than the keg"),
            Phrase("the scythe is remorseless"),
            Phrase("live by the sword die by the sword"),
            Phrase("the whole of it calls for tears"),
        ]
        self.missed = 0
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        self.replay = ""

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("------------------------")
        print("Welcome to Phrase Hunter")
        print("------------------------")
        print("""
Guess all the letters in a hidden phrase.

After five incorrect guesses, it's game over.

Good luck!""")

    def start(self):
        self.welcome()
        while self.replay == "" or self.replay == "y":
            self.active_phrase = self.get_random_phrase()       
            if self.replay == "y":
                self.guesses = []
                self.missed = 0
            while self.active_phrase.check_complete(self.guesses) == False and self.missed < 5:
                self.active_phrase.display(self.guesses)
                user_guess = self.get_guess()
                self.guesses.append(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    self.missed += 1
                    print("{} is not present. You have {} incorrect guesses.".format(user_guess, self.missed))
            else:
                self.game_over() 

    def get_guess(self):
        while True:
            try:
                user_guess = input("Guess a letter: ")
                user_guess = user_guess.lower()
                if user_guess < "a" or user_guess > "z":
                    raise ValueError("\nInvalid guess. Cannot be a number or a character.")
                elif len(user_guess) != 1:
                    raise ValueError("\nInvalid guess. Only enter one letter.")
                elif user_guess in self.guesses:
                    raise ValueError("\nYou've already guessed that letter.")
                break
            except ValueError as err:
                print("{}".format(err))
        return user_guess

    def game_over(self):
        if self.missed == 5:
            print("\n***You've used all your guesses***")
            print("GAME OVER")
        else:
            print("\n*** YOU WIN! ***")
            self.active_phrase.display(self.guesses)
        self.replay = input("\nPlay again? Y/N: ").lower()
        while self.replay != "y" and self.replay != "n":
            self.replay = input("\nInvalid entry. Play again? Y/N: ").lower()
        
            
        
