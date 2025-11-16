'''
File: main.py
Description: This is the main file that has the driver code and the test cases
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from animal import Mammal, Bird, Reptile, Animal
from enclosure import Enclosure
from staff import Veterinarian, Zookeeper

@pytest.fixture
def sample_animals():
    return {
        "lion": Mammal("Nala", "Lion", 5, "Meat", "Roar"),
        "parrot": Bird("Polly", "Parrot", 2, "Seeds", "Squawk"),
        "python": Reptile("Monty", "Python", 4, "Rodents", "Hiss")
    }

@pytest.fixture
def sample_staff():
    return {
        "vet": Veterinarian("Dr. Lee"),
        "keeper": Zookeeper("Jordan")
    }

@pytest.fixture
def sample_enclosures():
    return {
        "savannah": Enclosure("Savannah Plains", "Savannah", 1200),
        "aviary": Enclosure("Sky Haven", "Aviary", 800)
    }

@pytest.fixture
def generic_animal():
    return Animal("Simba", "Lion", 3, "Meat", "Roar")