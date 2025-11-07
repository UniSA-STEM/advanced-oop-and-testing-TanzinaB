'''
File: main.py
Description: This is the main file that has the driver code and the test cases
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Bird, Reptile, HealthRecord
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def main():
    print("\n=== Simone’s Zoo Management System (Final Version with Multiple Animal Types) ===\n")

    # Create animals
    lion = Mammal("Nala", "Lion", 5, "Meat", "Roar")
    koala = Mammal("Kiki", "Koala", 3, "Leaves", "Grunt")
    parrot = Bird("Polly", "Parrot", 2, "Seeds", "Squawk")
    python = Reptile("Monty", "Python", 4, "Rodents", "Hiss")

    # Create enclosures
    savannah = Enclosure("Savannah Plains", "Savannah", 1200)
    grove = Enclosure("Gumtree Grove", "Rainforest", 800)

    # Create staff
    keeper = Zookeeper("Jordan")
    vet = Veterinarian("Dr. Rivera")

    print(keeper.perform_duty())
    print(vet.perform_duty())

    # Assign animals
    savannah.add_animal(lion)
    grove.add_animal(koala)

    print("\n--- Daily Routine ---")
    print(keeper.feed(lion))
    print(keeper.clean_enclosure(savannah))
    print(lion.make_sound())
    print(koala.make_sound())
    print(parrot.make_sound())
    print(python.make_sound())

    print("\n--- Health System Demo ---")
    print(vet.diagnose(lion, "Sprained paw", 2))
    print(lion.health_status())
    try:
        grove.add_animal(lion)
    except ValueError as e:
        print("[Movement Blocked]", e)
    print(vet.treat(lion))
    print(lion.health_status())

    print("\n--- Running Internal Tests ---")
    run_internal_tests()

    print("\n=== End of Zoo Demo ===\n")


# === INTERNAL TESTS ===
def run_internal_tests():
    """Test suite showing data validation, error handling, and encapsulation."""
    print("\n[TEST 1] Invalid data validation:\n")
    try:
        Animal("", "Lion", 5, "Meat", "Roar")
    except ValueError as e:
        print("✅ Passed (empty name):", e)
    try:
        Animal("Simba", "", 5, "Meat", "Roar")
    except ValueError as e:
        print("✅ Passed (missing species):", e)
    try:
        Animal("Simba", "Lion", -3, "Meat", "Roar")
    except ValueError as e:
        print("✅ Passed (negative age):", e)

    print("\n[TEST 2] Enclosure validation:\n")
    try:
        Enclosure("", "Savannah", 1000)
    except ValueError as e:
        print("✅ Passed (empty name):", e)
    try:
        Enclosure("Tiny Cage", "Savannah", -50)
    except ValueError as e:
        print("✅ Passed (negative size):", e)

    print("\n[TEST 3] Health record validation:\n")
    record = HealthRecord()
    try:
        record.add_issue("", 3)
    except ValueError as e:
        print("✅ Passed (empty description):", e)
    try:
        record.add_issue("Fracture", 10)
    except ValueError as e:
        print("✅ Passed (invalid severity):", e)

    print("\n[TEST 4] Private method accessibility:\n")
    lion = Animal("Leo", "Lion", 6, "Meat", "Roar")
    enc = Enclosure("Grassland", "Grass", 900)
    enc.add_animal(lion)
    try:
        lion.__digest_food()
    except AttributeError as e:
        print("✅ Passed (cannot access private __digest_food):", e)
    try:
        enc.__sanitize()
    except AttributeError as e:
        print("✅ Passed (cannot access private __sanitize):", e)

    print("\n[TEST 5] Enclosure restrictions:\n")
    koala = Animal("Kiki", "Koala", 3, "Leaves", "Grunt")
    try:
        enc.add_animal(koala)
    except ValueError as e:
        print("✅ Passed (species restriction):", e)

    print("\n[TEST 6] Movement restriction for unwell animal:\n")
    vet = Veterinarian("Dr. Lee")
    vet.diagnose(lion, "Cough", 2)
    new_enc = Enclosure("New Plains", "Savannah", 1000)
    try:
        new_enc.add_animal(lion)
    except ValueError as e:
        print("✅ Passed (unwell animal blocked):", e)

    print("\n[TEST 7] Cleanliness increment:\n")
    before = enc.cleanliness
    enc.clean()
    after = enc.cleanliness
    print(f"✅ Passed: cleanliness increased from {before} to {after}")

    print("\n[TEST 8] Health record resolution:\n")
    rec = HealthRecord()
    rec.add_issue("Fever", 3)
    print("Before resolve:", rec.status())
    rec.resolve_all()
    print("After resolve:", rec.status())


if __name__ == "__main__":
    main()

