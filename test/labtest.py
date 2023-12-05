"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import unittest
import requests

from main.lab import classify


class TestLLMResponse(unittest.TestCase):

    """
    Your prompt should make the LLM correctly classify positive responses.
    """

    def test_classify_positive_1(self):
        result = classify("that was a great movie")
        self.assertIn("positive", result)
        self.assertNotIn("negative", result)

    """
    Your prompt should make the LLM correctly classify negative responses.
    """

    def test_classify_negative_1(self):
        result = classify("that was a terrible movie")
        self.assertIn("negative", result)
        self.assertNotIn("positive", result)

    """
    Your prompt should make the LLM correctly classify positive responses.
    """

    def test_classify_positive_2(self):
        result = classify("i love that this product has so many interesting features")
        self.assertIn("positive", result)
        self.assertNotIn("negative", result)

    """
    Your prompt should make the LLM correctly classify negative responses.
    """

    def test_classify_negative_2(self):
        result = classify("i don't like this product")
        self.assertIn("negative", result)
        self.assertNotIn("positive", result)

    """
    Your prompt should make the LLM correctly classify positive responses.
    """

    def test_classify_positive_3(self):
        result = classify("i thought i wouldn't like the show, but i was pleasantly surprised")
        self.assertIn("positive", result)
        self.assertNotIn("negative", result)

    """
    Your prompt should make the LLM correctly classify negative responses.
    """

    def test_classify_negative_3(self):
        result = classify("the show wasn't very impressive")
        self.assertIn("negative", result)
        self.assertNotIn("positive", result)

if __name__ == '__main__':
    unittest.main()
