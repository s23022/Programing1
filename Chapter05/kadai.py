# ユーザーから数字を入力
num = int(input("数字を入力してください: "))

# 自然数かどうかを判断
if num > 0:
    is_natural = True
else:
    is_natural = False

# 素数かどうかを判断
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    else:
        is_prime = True
else:
    is_prime = False

# 結果を出力
if is_natural:
    if is_prime:
        print(f"{num}は自然数で、素数です。")
    else:
        print(f"{num}は自然数ですが、素数ではありません。")
else:
    print(f"{num}は自然数ではありません。")
