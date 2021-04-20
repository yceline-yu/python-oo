from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """the file path provided"""
        self.file_path = file_path
        self.words = []
        self.read_file()

    def read_file(self):
        """reads the file and appends to a list"""
        file = open(self.file_path)
        for line in file:
            self.words.append(line.replace("\n",""))
        print(f"{len(self.words)} words read")

    def random(self):
        """return a random word from list"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder: handles blank lines and lines that start with #"""

    def read_file(self):
        """handles blanks and lines that start #"""
        file = open(self.file_path)
        for line in file:
            if line == "\n" or line[0] == "#": 
                continue
            else:
                self.words.append(line.replace("\n",""))
        print(f"{len(self.words)} words read")