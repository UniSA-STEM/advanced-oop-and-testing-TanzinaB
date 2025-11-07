'''
File: enclosure.py
Description: Handles cleanliness and species restrictions (encapsulation + validation)
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    """Represents an enclosure that holds compatible animals."""
    def __init__(self, name, environment, size):
        if not name or size <= 0:
            raise ValueError("Enclosure must have valid name and positive size.")
        self.__name = name.title()
        self.__environment = environment.lower()
        self.__size = size
        self.__cleanliness = 100
        self.__animals = []

    @property
    def name(self): return self.__name
    @property
    def cleanliness(self): return self.__cleanliness

    def add_animal(self, animal):
        if self.__animals and self.__animals[0].species != animal.species:
            raise ValueError(f"Cannot mix {animal.species} with {self.__animals[0].species}.")
        if animal.health.is_unwell():
            raise ValueError(f"{animal.name} is unwell and cannot be moved.")
        self.__animals.append(animal)
        animal.assign_enclosure(self)

    def clean(self):
        self.__sanitize()
        return f"{self.__name} cleaned. Cleanliness is now {self.__cleanliness}%."

    def __sanitize(self):
        """Private cleaning method (encapsulation)."""
        self.__cleanliness = min(100, self.__cleanliness + 25)