import unittest
import os
import threading
from custom_dictionary import CustomDictionary

class TestCustomDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = CustomDictionary()

    def test_add_and_search_word(self):
        self.dictionary.add_word("cat")
        self.dictionary.add_word("car")
        
        self.assertTrue(self.dictionary.search_word("cat"))
        self.assertTrue(self.dictionary.search_word("car"))
        self.assertFalse(self.dictionary.search_word("cab"))

    def test_remove_word(self):
        self.dictionary.add_word("cat")
        self.assertTrue(self.dictionary.remove_word("cat"))
        self.assertFalse(self.dictionary.search_word("cat"))
        self.assertFalse(self.dictionary.remove_word("cat"))  # Should not find it again

    def test_auto_complete(self):
        self.dictionary.add_word("cat")
        self.dictionary.add_word("car")
        self.dictionary.add_word("carbon")
        self.dictionary.add_word("dog")

        completions = self.dictionary.auto_complete("ca")

        self.assertIn("cat", completions)
        self.assertIn("car", completions)
        self.assertIn("carbon", completions)
        self.assertNotIn("dog", completions)

    def test_save_and_load(self):
        self.dictionary.add_word("apple")
        self.dictionary.add_word("banana")
        self.dictionary.add_word("grape")

        filename = "test_dictionary.txt"
        self.dictionary.save_to_file(filename)

        new_dict = CustomDictionary()
        new_dict.load_from_file(filename)

        self.assertTrue(new_dict.search_word("apple"))
        self.assertTrue(new_dict.search_word("banana"))
        self.assertTrue(new_dict.search_word("grape"))

        os.remove(filename)

    def test_thread_safety(self):
        def worker(dictionary, words_to_add, words_to_remove):
            for word in words_to_add:
                dictionary.add_word(word)
            for word in words_to_remove:
                dictionary.remove_word(word)

        words = ["thread", "safe", "test", "word", "concurrent"]
        threads = []

        # Spawns 5 threads that run "worker()" at the same time on the same dictionary instance
        for _ in range(5):
            thread = threading.Thread(target=worker, args=(self.dictionary, words, ["word"]))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Check that all added words (except "word") are present
        self.assertTrue(self.dictionary.search_word("thread"))
        self.assertTrue(self.dictionary.search_word("safe"))
        self.assertTrue(self.dictionary.search_word("test"))
        self.assertTrue(self.dictionary.search_word("concurrent"))
        # Check that "word" is not present
        self.assertFalse(self.dictionary.search_word("word"))

if __name__ == '__main__':
    unittest.main()
