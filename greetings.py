"""Fictional greeting example used solely for standalone workflow qualification."""


def greeting(name: str) -> str:
    """Greet a fictional visitor."""
    return f"Hello, {name.strip()}!"


def farewell(name: str) -> str:
    """Say goodbye to a fictional visitor."""
    return f"Goodbye, {name.strip()}!"
