"""dict_1 = {"name": "Alice", "age": 30, "city": "New York"}
a = dict_1["name"]
print(f"a: {a}")
b = dict_1.get("age")
print(f"b: {b}")
dict_1["age"] = 31
print(f"Updated age: {dict_1['age']}")
dict_1["profession"] = "Engineer"
print(f"Added profession: {dict_1['profession']}")
print("Iterating through dictionary keys and values:")
for key in dict_1:
    print(f"{key}: {dict_1[key]}")
for key, value in dict_1.items():
    print(f"{key}: {value}")"""
dict_1 = {"name": "Alice", "age": 30, "city": "New York"}
a = dict_1["age"]
dict_1["age"] = 31
print(f"Updated age: {dict_1['age']}")
dict_1["profession"] = "Engineer"
dict_1["hobby"] = "Photography"
dict_1["dislikes"] = "Loud noises"
print(dict_1)
del dict_1["dislikes"]
c = dict_1.keys()
print(c)
d = dict_1.values()
print(d)
e = dict_1.items()
print(e)