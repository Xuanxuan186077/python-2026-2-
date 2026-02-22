from decimal import Decimal
money = input("请输入您充值的金额：")
the_user = input("请问您是新用户吗？(是/否)：")
money = Decimal(money)
result_money = money
if money < 1000:
    result_money = money
elif money <= 2000:
    result_money += money * Decimal("0.15")
    if money > 5000:
        result_money += money * Decimal("0.2") + Decimal("500")
        if money > 10000:
            result_money += 1000
if the_user == "是":
    result_money = money * Decimal("1.1")
else:
    result_money = money
print("充值金额：", result_money)