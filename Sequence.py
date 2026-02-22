import time
def callback_function():
    """
    该函数是一个回调函数, 用于在进度条完成时执行
    注意该函数没有函数输入，需要你自己实现

    :param: None 

    :return: None
    """
    print("回调函数执行: 进度条已完成")
    return None

def progress_function(seconds, callback_function):
    """
    该函数是一个进度条示例函数, 每0.1秒打印一个进度条, 直到100%
    注意该函数没有函数输入，需要你自己实现

    :param: None 

    :return: None
    """
    count = 0
    while count < 100:
        count += 1
        progress = '■' * count + '□' * (100 - count)
        print(progress, end='\r')
        time.sleep(seconds) # 模拟耗时操作, 这里time.sleep(0.1)代表程序暂停0.1s
        
        if count == 100:
           callback_function()  # 调用回调函数
    return None


my_list = [ "这是一个字符串", 6732123, ["计算机", "机器人", "自动化"],
           "", 12.9682, 6+9j, ["清华大学", "浙江大学"], "Apple",progress_function(0.1, callback_function), callback_function() ]
my_new_list = []
for index in range (7, -1, -1):
    my_new_list.append(my_list[index])
print(f"my_new_list is {my_new_list}")
# 删除列表中的所有元素
count = 0
while count < 10:
    my_list.pop(0)
    count += 1
print(my_list)