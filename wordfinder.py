from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

        >>> wf = WordFinder("test.txt")
        3 words read
        >>> wf.random()
        'words'

    """

    def __init__(self, file_path):
        """the file path provided"""
        # self.file_path = file_path
        self.words = []
        file = open(file_path)
        self.read_file(file)
        print(f"{len(self.words)} words read")

    def read_file(self, file):
        """reads the file and appends to a list"""
        for line in file:
            self.words.append(line.replace("\n",""))

    def random(self):
        """return a random word from list"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder: handles blank lines and lines that start with #"""

    def read_file(self, file):
        """handles blanks and lines that start #"""
        for line in file:
            if line == "\n" or line[0] == "#":
                continue
            else:
                self.words.append(line.replace("\n",""))
