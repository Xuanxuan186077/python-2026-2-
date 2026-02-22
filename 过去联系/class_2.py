class animal():
    name = ""
    spcies = ""
    age = 0
    eat_times_everyday = 0
    

dog = animal()
dog.name = "Buddy"
dog.spcies = "Dog"
dog.age = 5
dog.eat_times_everyday = 3
cat = animal()
cat.name = "Whiskers"
cat.spcies = "Cat"
cat.age = 3
cat.eat_times_everyday = 2
print (f"Animal Name: {dog.name}, Species: {dog.spcies}, Age: {dog.age}, Eat Times Everyday: {dog.eat_times_everyday}")
print (f"Animal Name: {cat.name}, Species: {cat.spcies}, Age: {cat.age}, Eat Times Everyday: {cat.eat_times_everyday}")
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print (f"my_dict['name'] is {my_dict['name']}")
print (f"my_dict['age'] is {my_dict['age']}")
print (f"my_dict['city'] is {my_dict['city']}")
import class_3
animal_list = class_3.person(name = "Alice", age = 30, sex = "female")