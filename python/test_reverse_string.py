import unittest

from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    def test_reverses_hello(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverses_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverses_one_letter(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverses_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")


if __name__ == "__main__":
    unittest.main()