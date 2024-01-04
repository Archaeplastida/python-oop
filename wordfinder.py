from random import randint

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, file):
        self.file = open(file, "r")
        self.line_count = 0
        for x in self.file:
            self.line_count += 1
        self.file.seek(0)

    def random(self):
        self.file.seek(0)
        self.chosen_line = self.file.readlines()[randint(0,self.line_count-1)]
        return self.chosen_line.strip()
    
class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)

    def random(self):
        self.file.seek(0)
        self.chosen_line = self.file.readlines()[randint(0,self.line_count-1)]
        while self.chosen_line.strip().startswith("#") or len(self.chosen_line) == 0:
            self.chosen_line = self.file.readlines()[randint(0,self.line_count-1)]
        return self.chosen_line.strip()