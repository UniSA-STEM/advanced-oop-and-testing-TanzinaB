'''
File: main.py
Description: This is the main file that has the driver code and the test cases
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from animal import Reptile
from enclosure import Enclosure
from species import Lion, Koala, Penguin

def main():
    print("=== Simone's Zoo Management System ===\n")

    lion = Lion("Hero", "Lion", 5, "Meat")
    koala = Koala("Kiki", "Koala", 3, "Eucalyptus Leaves")
    penguin = Penguin("Pingu", "Penguin", 4, "Fish")

    savannah = Enclosure("Savannah Plains", "Savannah", 1200)
    eucalyptus = Enclosure("Gumtree Grove", "Rainforest", 800)

    # Add animals

    savannah.add_animal(lion)
    eucalyptus.add_animal(koala)

