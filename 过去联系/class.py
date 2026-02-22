class animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Cat(animal):
    def speak(self):
        return f"{self.name} says Meow!"
class Cow(animal):
    def speak(self):
        return f"{self.name} says Moo!"
class Sheep(animal):
    def speak(self):
        return f"{self.name} says Baa!"
class Pig(animal):
    def speak(self):
        return f"{self.name} says Oink!"
class Chicken(animal):
    def speak(self):
        return f"{self.name} says Cluck!"
class Duck(animal):
    def speak(self):
        return f"{self.name} says Quack!"
print ("Animal Sounds:")
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Cow("Bessie"),
    Sheep("Dolly"),
    Pig("Porky"),
    Chicken("Clucky"),
    Duck("Donald")
]
for animal in animals:
    print(animal.speak())