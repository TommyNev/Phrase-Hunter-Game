# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        print_phrase = ""
        for character in self.phrase:
            if character in guesses or character == " ":
                character = "{} ".format(character)
                print_phrase += character
            else:
                print_phrase += "_ "
        print("\n\nPHRASE:", print_phrase,)

    def check_guess(self, guess):
        return guess in self.phrase

    def check_complete(self, guesses):
        for character in self.phrase.replace(" ", ""):
            if character not in guesses:
                return False
        else:
            return True
