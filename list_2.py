my_list = [1, 2, 3, 4, 5]
for index in range (0, len(my_list)):
    print(my_list[index])
my_list.append(6)
my_list.remove(1)
my_list.pop(2)
del my_list[0]
print(my_list)
my_list.extend([6,8,4,5])
my_list.append([7, 8, 9])
print(my_list)