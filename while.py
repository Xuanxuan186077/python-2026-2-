import random
count = 0
the_right_num = random.randint(1, 150000)
my_num = int(input("请输入您猜想的数字："))
while my_num != the_right_num:
    if my_num <the_right_num:
        my_num = (my_num + the_right_num) / 2
    elif my_num > the_right_num:
        my_num = (my_num + the_right_num) / 2
    count += 1
    print(f"你猜了 {count} 次")
print("恭喜你，猜对了！")