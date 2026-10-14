"""Deterministic checks; no agents or network access."""
import unittest
from greetings import farewell, greeting


class GreetingTests(unittest.TestCase):
    def test_named_visitor(self):
        self.assertEqual(greeting("  Harbor  "), "Hello, Harbor!")

    def test_farewell_named_visitor(self):
        self.assertEqual(farewell("  Harbor  "), "Goodbye, Harbor!")


if __name__ == "__main__":
    unittest.main()
