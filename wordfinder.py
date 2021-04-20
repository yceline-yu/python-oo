class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.words = []
        self.read_file()

    def read_file(self):
        file = open(self.file_path)
        for line in file:
            self.words.append(line)
        print(f"{len(self.words)} words read")
