'''
File: enclosure.py
Description: Handles cleanliness and species restrictions (encapsulation + validation)
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    """Holds animals of one species and maintains cleanliness."""
    def __init__(self, name: str, environment: str, size: float):
        if not name or size <= 0:
            raise ValueError("Valid name and positive size required.")
        self._name = name.title()
        self._environment = environment.lower()
        self._size = size
        self._animals = []
        self._cleanliness = 100  # 0–100 scale

    @property
    def name(self): return self._name
    @property
    def animals(self): return list(self._animals)
    @property
    def cleanliness(self): return self._cleanliness

    def add_animal(self, animal):
        """Add an animal if compatible."""
        if self._animals and self._animals[0].species != animal.species:
            raise ValueError(f"Cannot mix {animal.species} with {self._animals[0].species}!")
        if animal.health.is_unwell():
            raise ValueError(f"{animal.name} is unwell and cannot be moved.")
        self._animals.append(animal)
        animal.assign_enclosure(self)

    def clean(self):
        self._cleanliness = min(100, self._cleanliness + 30)
        return f"{self._name} enclosure cleaned. Cleanliness now {self._cleanliness}."

    def status_report(self):
        animal_names = ", ".join([a.name for a in self._animals]) or "No animals"
        return f"{self._name} | Cleanliness: {self._cleanliness}% | Animals: {animal_names}"