"""Deterministic checks; no agents or network access."""
import unittest
from greetings import greeting


class GreetingTests(unittest.TestCase):
    def test_named_visitor(self):
        self.assertEqual(greeting("  Harbor  "), "Hello, Harbor!")

    def test_empty_name(self):
        self.assertEqual(greeting(""), "Hello, friend!")

    def test_whitespace_only_name(self):
        self.assertEqual(greeting(" \t\n "), "Hello, friend!")


if __name__ == "__main__":
    unittest.main()
