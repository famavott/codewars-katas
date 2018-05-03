"""Class example."""


class Player(object):
    """Hockey player class inheriting from object."""

    def __init__(self, salary=100, team=None):
        """Create instance of Player Class."""
        self.salary = salary
        self.team = team
