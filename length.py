my_list = ["apple", "banana", "cherry", "date", ["elderberry", "fig", "grape"], isinstance(42, int)]
for item in my_list:
    print(f"item{my_list.index(item)}: {item}")
length = 0
while length < len(my_list):
    print(f"the item {length}: {my_list[length]}")
    length += 1