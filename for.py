# sum = 0
# num = 1
# while num <= 1000000:
#     if num % 2 == 0:
#         sum += num
#     num += 1
# print("1到1000000之间的偶数和为：", sum)
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} * {j} = i * j", end="\t")
    print()