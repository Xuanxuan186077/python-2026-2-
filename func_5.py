def check_fermat(max_val, n):
    """
    在 1 到 max_val 的范围内尝试寻找 x^n + y^n = z^n 的解
    """
    if n <= 2:
        print("n 必须大于 2 才能验证费马大定理。")
        return

    found_solution = False
    
    # 嵌套循环遍历所有可能的 x, y, z
    for x in range(1, max_val + 1):
        for y in range(1, max_val + 1):
            for z in range(1, max_val + 1):
                # 计算等式两边
                if x**n + y**n == z**n:
                    print(f"居然找到了！解为: {x}^{n} + {y}^{n} = {z}^{n}")
                    found_solution = True
    
    if not found_solution:
        print(f"在 1 到 {max_val} 的范围内，未发现 n={n} 的解。费马看起来是对的！")

# 尝试验证 n=3，在 1-100 范围内搜索
check_fermat(10000000000000000000000000000000000000000000, 73)