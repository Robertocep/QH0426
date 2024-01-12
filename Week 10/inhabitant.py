# Use the following starting template for the class Inhabitant to implement the functionality
# as described above by moving common attributes and methods to the class Inhabitant.
# You should also add suitable implementations for the functions __repr__ and __str__ to your class.
# Your file should be stored in the following location: oop/inhabitant.py

# from abc import ABC

class Inhabitant:
    MAX_ENERGY = 100

    def __init__(self, name= "inhabitant", age=0,):
    self.name = name


    class Human(Inhabitant)