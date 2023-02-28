import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    # Test for null input for englishToFrench
    def test_englishToFrench_with_null_input(self):
        self.assertEqual(english_to_french(None), None)

    # Test for the translation of the word ‘Hello’
    def test_englishToFrench_with_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    # Test for null input for frenchToEnglish
    def test_frenchToEnglish_with_null_input(self):
        self.assertEqual(french_to_english(None), None)

    # Test for the translation of the word ‘Bonjour’
    def test_frenchToEnglish_with_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
