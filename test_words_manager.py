import unittest

from words_manager import WordsManager


class TestFindMethod(unittest.TestCase):
    def test_find_one(self):
        words = ["helloworld", "foo", "bar", "stylight_team", "seo"]
        manager = WordsManager(words)
        word_to_search = "eos"
        actual = manager.find(word_to_search)
        expected = ["seo"]
        self.assertEqual(actual, expected)

    def test_find_multiple(self):
        words = ["helloworld", "foo", "eso", "stylight_team", "seo"]
        manager = WordsManager(words)
        word_to_search = "eos"
        actual = manager.find(word_to_search)
        expected = ["eso", "seo"]
        self.assertEqual(actual, expected)

    def test_empty_word_list(self):
        words = []
        manager = WordsManager(words)
        word_to_search = "eos"
        self.assertRaises(ValueError, manager.find(word_to_search))

    def test_empty_string_to_search(self):
        words = ["helloworld", "foo", "eso", "stylight_team", "seo"]
        manager = WordsManager(words)
        word_to_search = ""
        actual = manager.find(word_to_search)
        expected = []
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
