'''
File: animal.py
Description: Demonstrates encapsulation, inheritance, polymorphism and composition
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name:str, species:str, age:int, diet:str):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet

    def eat(self):
        return f"{self.name}, the {self.species} is eating {self.diet}"

    def sound(self):
        return f"{self.name}, the {self.species} is making sound"

    def sleep(self):
        return f"{self.name}, the {self.species} is sleeping"

    def feel_sick(self):
        pass

    def feel_ok(self):
        pass

class Mammal(Animal):
    def __init__(self, name, species, age, diet, has_hair:bool):
        super().__init__(name, species, age, diet)
        self.has_hair = True


class Reptile(Animal):
    def __init__(self, name, species, age, diet, has_scale:bool):
        super().__init__(name, species, age, diet)
        self.has_scale = True

    def crawl(self):
        pass

class Birds(Animal):
    def __init__(self, name, species, age, diet, has_beak:bool, wing_span):
        super().__init__(name, species, age, diet)
        self.has_beak = True
        self.wing_span = wing_span

    def fly(self):
        pass