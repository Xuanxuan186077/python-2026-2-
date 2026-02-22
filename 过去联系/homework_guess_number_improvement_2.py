import random

def binary_search_guess():
    # 生成随机数
    target = random.randint(1, 1000000000000000000000000)
    count = 0
    low = 1
    high = 1000000000000000000000000

    # 使用二分查找进行猜测
    while low <= high:
        count += 1
        mid = (low + high) // 2
        
        if mid == target:
            print(f"恭喜您，猜对了！您一共猜了{count}次，正确数字是{target}。")
            break
        elif mid > target:
            high = mid - 1
        else:
            low = mid + 1

if __name__ == "__main__":
    binary_search_guess()