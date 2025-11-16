'''
File: animal.py
Description: Demonstrates encapsulation, inheritance, polymorphism and composition
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

from datetime import date

class HealthRecord:
    """Tracks health issues and treatments for an animal (composition)."""
    def __init__(self):
        self.__issues = []

    def add_issue(self, description: str, severity: int):
        if not description or not (1 <= severity <= 5):
            raise ValueError("Valid description and severity (1–5) required.")
        self.__issues.append({
            "description": description,
            "severity": severity,
            "resolved": False,
            "date": date.today()
        })

    def resolve_all(self):
        for issue in self.__issues:
            issue["resolved"] = True

    def is_unwell(self):
        return any(not issue["resolved"] for issue in self.__issues)

    def status(self):
        if not self.__issues:
            return "Healthy"
        active = [i for i in self.__issues if not i["resolved"]]
        return "Under treatment" if active else "Recovered"


class Animal:
    """Base animal class demonstrating encapsulation and composition."""
    def __init__(self, name, species, age, diet, sound):
        if not name or not species:
            raise ValueError("Animal name and species are required.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.__name = name.title()
        self.__species = species.lower()
        self.__age = age
        self.__diet = diet
        self.__sound = sound
        self.__health = HealthRecord()
        self.__enclosure = None

    @property
    def name(self): return self.__name
    @property
    def species(self): return self.__species
    @property
    def health(self): return self.__health

    def assign_enclosure(self, enclosure):
        self.__enclosure = enclosure

    def eat(self):
        return f"{self.__name} eats {self.__diet}. {self.__digest_food()}"

    def __digest_food(self):
        """Private helper method for encapsulation."""
        return f"{self.__name} quietly digests {self.__diet}."

    def make_sound(self):
        """Default behaviour (can be overridden)."""
        return f"{self.__name} makes a '{self.__sound}' sound."

    def health_status(self):
        return f"{self.__name} is {self.__health.status()}."


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} (mammal) says '{self._Animal__sound}'."


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} (bird) chirps '{self._Animal__sound}'."


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} (reptile) hisses '{self._Animal__sound}'."