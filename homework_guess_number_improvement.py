import random
# 1. 生成一个随机数
the_right_num = random.randint(1, 10000000000000000)
count = 0
low = 1
high = 10000000000000000
# 2. 进行猜测
while True:
    my_num = random.randint(low, high)
    count += 1
    if my_num > the_right_num:
        high = my_num - 1
    elif my_num < the_right_num:
        low = my_num + 1
    else:
        break
# 3. 输出结果
print(f"恭喜您，猜对了！您一共猜了{count}次，正确数字是{the_right_num}。")