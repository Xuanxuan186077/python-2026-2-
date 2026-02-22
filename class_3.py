class person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        return None
        
    def __str__(self):
        return f"Person Name: {self.name}, Age: {self.age}, Sex: {self.sex}"        
    
    
Person = person(name = "Alice", age = 30, sex = "female")
print(Person)