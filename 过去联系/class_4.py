class animal():
    def __init__(self, name, age ,hobby,sound ,species):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.sound = sound
        self.species = species
        return None
    def description(self):
        return f"Animal Name: {self.name}, Age: {self.age}, Hobby: {self.hobby}, Species: {self.species}, Sound: {self.sound}"
    def __str__(self):
        return self.description()
    def __add__(self, other):
        return f"{self.name} and {other.name} are friends."
    def __sub__(self, other):
        return f"{self.name} and {other.name} are not friends."
    def __mul__(self, other):
        return f"{self.name} and {other.name} have a combined age of {self.age + other.age} years."
    def __truediv__(self, other):
        return f"{self.name} and {other.name} have an average age of {(self.age + other.age) / 2} years."
    def __eq__(self, value):
        if isinstance(value, animal):
            return self.name == value.name
        return False
    def make_sound(self):
        print (f"{self.name} says {self.sound}")
    def __call__(self):
        self.make_sound()
        
    
    
    

dog = animal(name = "Buddy", age = 5, hobby = "Playing fetch", species = "Dog", sound = "Woof")
cat = animal(name = "Whiskers", age = 3, hobby = "Chasing mice", species = "Cat", sound = "Meow")
import random