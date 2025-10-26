'''
File: filename.py
Description: A brief description of this Python module.
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
    def

class Reptile(Animal):
    def


class Birds(Animal):
    def