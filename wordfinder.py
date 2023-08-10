"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, file_path):
        self.word_list = self._read_words(file_path)
        self.num_words = len(self.word_list)
    
    def _read_words(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
        
if __name__ == '__main__':
    word_list = WordList('path_file.txt')
    print(f"{word_list.num_words} words read")

    for x in range(5):
        print(word_list.random())

class SpecialWordFinder(WordList):
    def _read_words(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip() and not line.startswith("#")]

if __name__ == "__main__":
    special_word_finder = SpecialWordFinder("path_to_your_file.txt")
    print(f"{special_word_finder.num_words} words read")

    for _ in range(5):
        print(special_word_finder.random())
