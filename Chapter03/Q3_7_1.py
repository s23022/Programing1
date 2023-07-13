import random

target = "".join(random.sample("0123456789", 4))
print("Target:", target)

while input("4桁の数字を入力: ") != target:
    print("不正解です。もう一度")

print("正解")
