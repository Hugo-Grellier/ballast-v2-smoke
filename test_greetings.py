"""Deterministic checks; no agents or network access."""
import unittest
from greetings import greeting, shout


class GreetingTests(unittest.TestCase):
    def test_named_visitor(self):
        self.assertEqual(greeting("  Harbor  "), "Hello, Harbor!")

    def test_shouted_visitor(self):
        self.assertEqual(shout("  Harbor  "), "HELLO, HARBOR!")


if __name__ == "__main__":
    unittest.main()
