class WordsManager:
    def __init__(self, words):
        self.words = words
        self.word_counter = {}
        for word in words:
            word_key = "".join(sorted(word))
            self.word_counter[word_key] = self.word_counter.get(word_key, []) + [word]

    def find(self, word_to_find):
        if not self.words:
            raise ValueError("Words array cannot be empty")
        if not word_to_find:
            return []

        word_key = "".join(sorted(word_to_find))
        return self.word_counter.get(word_key, [])
