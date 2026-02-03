from abc import ABC, abstractmethod

# Abstraction & Inheritance: Individual is an abstract base class that provides a common interface
# Subclasses inherit shared attributes/behavior from Individual.
class Individual(ABC):
    def __init__(self, name):
        self._name = name  # Protected attribute (supports encapsulation in subclasses)

    @abstractmethod
    def display(self):
        """Return a string representation of the individual."""
        pass