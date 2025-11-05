'''
File: staff.py
Description: Abstract base Staff class and two concrete subclasses (inheritance and polymorphism)
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__(self, jobType):
        self.jobType = jobType

    def health_check(self):
        pass

    def feed_animals(self):
        pass

    def clean_enclosures(self):
        pass