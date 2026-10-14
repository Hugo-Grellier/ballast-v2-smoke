"""Fictional greeting example used solely for standalone workflow qualification."""


def greeting(name: str) -> str:
    """Greet a fictional visitor."""
    return f"Hello, {name.strip()}!"


def shout(name: str) -> str:
    """Greet a fictional visitor in upper case."""
    return greeting(name).upper()
