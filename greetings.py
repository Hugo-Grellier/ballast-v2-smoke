"""Fictional greeting example used solely for standalone workflow qualification."""


def greeting(name: str) -> str:
    """Greet a fictional visitor."""
    name = name.strip()
    return f"Hello, {name or 'friend'}!"
