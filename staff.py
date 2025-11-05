'''
File: staff.py
Description: Abstract base Staff class and two concrete subclasses (inheritance and polymorphism)
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name, role):
        if not name or not role:
            raise ValueError("Staff name and role required.")
        self._name = name.title()
        self._role = role.title()

    @property
    def name(self): return self._name
    @property
    def role(self): return self._role

    @abstractmethod
    def perform_duty(self):
        pass


class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def perform_duty(self):
        return f"{self.name} feeds animals and cleans enclosures."

    def feed(self, animal):
        return f"{self.name} feeds {animal.name}. {animal.eat()}"

    def clean_enclosure(self, enclosure):
        return f"{self.name} cleans {enclosure.name}. {enclosure.clean()}"


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def perform_duty(self):
        return f"{self.name} checks and treats animal health."

    def diagnose(self, animal, issue, severity):
        animal.health.add_issue(issue, severity)
        return f"{self.name} diagnosed {animal.name} with '{issue}'."

    def treat(self, animal):
        animal.health.resolve_all()
        return f"{self.name} treated {animal.name}. All issues resolved."