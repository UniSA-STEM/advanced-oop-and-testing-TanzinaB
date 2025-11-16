'''
File: main.py
Description: This is the main file that has the driver code and the test cases
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def main():
    print("\n=== Simone’s Zoo Management System Demo ===\n")

    # Create animals
    lion = Mammal("Nala", "Lion", 5, "Meat", "Roar")
    parrot = Bird("Polly", "Parrot", 2, "Seeds", "Squawk")
    python = Reptile("Monty", "Python", 4, "Rodents", "Hiss")

    # Create enclosures
    savannah = Enclosure("Savannah Plains", "Savannah", 1000)
    aviary = Enclosure("Sky Have", "Aviary", 500)

    # Create staff
    keeper = Zookeeper("Jordan")
    vet = Veterinarian("Dr. Rivera")

    print(keeper.perform_duty())
    print(vet.perform_duty())

    # Assign animals
    savannah.add_animal(lion)
    aviary.add_animal(parrot)

    print("\n--- Daily Routine ---")
    print(keeper.feed(lion))
    print(keeper.clean_enclosure(savannah))
    print(lion.make_sound())
    print(parrot.make_sound())
    print(python.make_sound())

    print("\n--- Health System Demo ---")
    print(vet.diagnose(lion, "Sprained paw", 2))
    print(lion.health_status())
    print(vet.treat(lion))
    print(lion.health_status())

if __name__ == "__main__":
    main()

