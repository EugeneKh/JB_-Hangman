from random import randint
from string import ascii_lowercase


class Game:
    words = ['python', 'java', 'kotlin', 'javascript']

    def __init__(self):
        self.word = ""
        self.letters = []
        print("H A N G M A N")
        while self.menu():
            pass

    def menu(self):
        command = input('Type "play" to play the game, "exit" to quit: ')
        if command == "play":
            self.play()
        elif command == "exit":
            return 0
        else:
            return 1

    def play(self):
        lives = 8
        word_id = randint(0, 3)
        self.word = self.words[word_id]
        self.letters = []
        while lives:
            print("")
            print(self.get_word())
            lives = lives + self.attempt()
            if self.check_win():
                print(f"You guessed the word {self.get_word()}!")
                break
        if not self.check_win():
            print("You lost!\n")
        else:
            print("You survived!\n")
        self.menu()

    def check_letter(self, letter):
        if len(letter) != 1:
            print("You should input a single letter")
            return False
        if letter in self.letters:
            print("You've already guessed this letter")
            return False
        if letter not in ascii_lowercase:
            print("Please enter a lowercase English letter")
            return False
        return True

    def attempt(self) -> int:
        char = input("Input a letter:")
        if self.check_letter(char):
            self.letters.append(char)
            if char not in self.word:
                print("That letter doesn't appear in the word")
                return -1
            return 0
        else:
            return 0

    def get_word(self) -> str:
        s = []
        for ch in self.word:
            if ch in self.letters:
                s.append(ch)
            else:
                s.append("-")
        return "".join(s)

    def check_win(self):
        return "-" not in self.get_word()


g = Game()
