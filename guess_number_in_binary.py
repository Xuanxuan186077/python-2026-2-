import random
answer = random.randint(1,10000)
def binary(low_number, high_number):
    the_middle_num = int(low_number + high_number) / 2
    return the_middle_num
def binary_function(low_number,high_number,binary):
    """这是一个函数，用来定义二分法，从而在之后的程序编写中，能够实现快速的猜测‘
    number’功能。
    通过二分法猜测数字的范围在low_number和high_number之间。
    通过不断地将范围缩小一半，直到找到目标数字。
    :param low_number: 范围的下限
    :param high_number: 范围的上限
    :return: 返回猜测的数字和次数
    """
    guess_count = 0
    while answer != binary(low_number, high_number):
        if answer < binary(low_number, high_number):
            high_number = int(binary(low_number, high_number) - 1)
        else:
            low_number = int(binary(low_number, high_number) + 1)
        guess_count += 1
    return binary(low_number, high_number), guess_count

result = binary_function(1, 10000, binary)
print(f"猜测的数字是:{result[0]},猜测次数为{result[1]}次")