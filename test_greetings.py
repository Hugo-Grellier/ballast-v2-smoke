"""Deterministic checks; no agents or network access."""
import unittest
from greetings import greeting


class GreetingTests(unittest.TestCase):
    def test_named_visitor(self):
        self.assertEqual(greeting("  Harbor  "), "Hello, Harbor!")


if __name__ == "__main__":
    unittest.main()
