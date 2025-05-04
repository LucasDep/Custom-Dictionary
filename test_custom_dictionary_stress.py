import unittest
import random
import string
from custom_dictionary import CustomDictionary

class StressTestCustomDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = CustomDictionary()

    def random_word(self, length=8):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def test_add_and_search_many_words(self):
        words = {self.random_word() for _ in range(5000)}  # Create 5000 random words

        for word in words:
            self.dictionary.add_word(word)

        # Ensure all words are correctly searchable
        for word in words:
            self.assertTrue(self.dictionary.search_word(word))

    def test_auto_complete_large_prefix(self):
        base = 'testword'
        for i in range(1000):
            self.dictionary.add_word(f"{base}{i}")

        completions = self.dictionary.auto_complete('test')
        self.assertEqual(len(completions), 1000)
        self.assertTrue(all(word.startswith('test') for word in completions))

if __name__ == "__main__":
    unittest.main()
