import random
# 1. 生成一个随机数
the_right_num = random.randint(1,1000000000000000000000)
my_num = 0
count = 0
while True:
    my_num = random.randint(1,1000000000000000000000)
    if my_num > the_right_num:
        print("您所猜测的数字大了，请重新猜测：")
        my_num -= 1
    elif my_num < the_right_num:
        print("您所猜测的数字小了，请重新猜测：")
        my_num += 1
    else:
        print("恭喜您，猜对了！")
        break
    count += 1
    print("您猜测的次数为：", count)
    