def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# ジェネレーターを使用して素数を生成
prime_gen = prime_generator()

# 最初の10個の素数を表示
for _ in range(10):
    print(next(prime_gen))
