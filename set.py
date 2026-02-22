# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# for key in my_dict.keys():
#     print(f"Key: {key}, Value: {my_dict[key]}")
# my_dict["country"] = "USA"  # 添加新键值对
# my_dict["age"] = 31  # 修改现有键的值
# my_dict.pop("city")  # 删除键值对
# print(f"Updated dictionary: {my_dict}")
# my_dict_list = list(my_dict.items())  # 将字典转换为列表
# print(f"Dictionary as list of tuples: {my_dict_list}")
# my_dict_list.reverse()  # 反转列表
# print(f"Reversed list of tuples: {my_dict_list}")
my_list = [126, 5462, 3.1556, 41.243, 5.2105]
my_new_list = sorted(my_list, reverse=True)
print(f"my_new_list is {my_new_list}")
