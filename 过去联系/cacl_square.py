def calculate_square(number):
    a = number ** 2
    print(f"您所输入数字的平方为：{a}")
    return a
def calculate_cube(num):
    b = num ** 3
    print(f"您所输入数字的立方为：{b}")
    return b
def calculate_func(n):
    c = calculate_square(n)
    d = calculate_cube(n)
    return c, d

print("欢迎使用平方计算器")
print("请输入一个数字：")
num = float(input())
defm = calculate_func(num)
print(defm)
print("感谢使用，再见！")