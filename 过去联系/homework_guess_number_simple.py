import random
the_right_num = random.randint(1,40)
my_guess_num = int(input("请输入您所猜测的数字："))
while my_guess_num != the_right_num:
    if my_guess_num < the_right_num:
        print("您所猜测的数字小了，请重新猜测：")
    elif my_guess_num > the_right_num:
        print("您所猜测的数字大了，请重新猜测：")
    my_guess_num = int(input("请输入您所猜测的数字："))
print("恭喜您，猜对了！")