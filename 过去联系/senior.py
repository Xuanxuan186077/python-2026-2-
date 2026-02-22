str_1 = "这是一个字符串"
a = str_1.index("是")
b = str_1.find("是")
print(f"字符串中'是'的索引位置是: {a}, 使用find方法找到的位置是: {b}")
my_str = "Hello Alice, welcome to the world of Python!"
my_str_list = list(my_str)
my_list = my_str.split("o")
print(f"my_str_list is {my_str_list}")
print(f"my_list is {my_list}")
my_str = "Hello Alice, welcome to the world of Python!"
my_new_list = my_str[0:15:1]  # 反转字符串
print(f"my_new_list is {my_new_list}")