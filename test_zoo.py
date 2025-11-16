'''
File: main.py
Description: This is the main file that has the driver code and the test cases
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from animal import Animal, Mammal, Bird, Reptile, HealthRecord
from enclosure import Enclosure
from staff import Veterinarian

# ---------- Test Class 1: Data Validation ----------
class TestValidation:
    def test_invalid_animal_data(self):
        with pytest.raises(ValueError):
            Animal("", "Lion", 5, "Meat", "Roar")
        with pytest.raises(ValueError):
            Animal("Simba", "", 5, "Meat", "Roar")
        with pytest.raises(ValueError):
            Animal("Simba", "Lion", -1, "Meat", "Roar")

    def test_invalid_enclosure_data(self):
        with pytest.raises(ValueError):
            Enclosure("", "Savannah", 500)
        with pytest.raises(ValueError):
            Enclosure("Tiny Cage", "Grass", -100)

    def test_invalid_healthrecord_data(self):
        rec = HealthRecord()
        with pytest.raises(ValueError):
            rec.add_issue("", 3)
        with pytest.raises(ValueError):
            rec.add_issue("Broken wing", 10)

# ---------- Test Class 2: Encapsulation ----------
class TestEncapsulation:
    def test_private_methods_not_accessible(self, generic_animal):
        with pytest.raises(AttributeError):
            generic_animal.__digest_food()
        enc = Enclosure("Savannah Plains", "Savannah", 1000)
        with pytest.raises(AttributeError):
            enc.__sanitize()

# ---------- Test Class 3: Functionality ----------
class TestFunctionality:
    def test_species_restriction(self, sample_animals):
        lion = sample_animals["lion"]
        parrot = sample_animals["parrot"]
        enc = Enclosure("Savannah", "Savannah", 1000)
        enc.add_animal(lion)
        with pytest.raises(ValueError):
            enc.add_animal(parrot)

    def test_unwell_animal_cannot_move(self, sample_animals, sample_staff):
        lion = sample_animals["lion"]
        vet = sample_staff["vet"]
        vet.diagnose(lion, "Cough", 2)
        new_enc = Enclosure("New Plains", "Savannah", 1000)
        with pytest.raises(ValueError):
            new_enc.add_animal(lion)

    def test_cleanliness_increases(self, sample_animals):
        enc = Enclosure("Grassland", "Savannah", 800)
        lion = sample_animals["lion"]
        enc.add_animal(lion)
        before = enc.cleanliness
        enc.clean()
        after = enc.cleanliness
        assert after > before

# ---------- Test Class 4: Health Record ----------
class TestHealthRecord:
    def test_add_and_resolve_issue(self):
        rec = HealthRecord()
        rec.add_issue("Fever", 3)
        assert rec.status() == "Under treatment"
        rec.resolve_all()
        assert rec.status() == "Recovered"