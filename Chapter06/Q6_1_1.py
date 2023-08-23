class Cat:
    def __init__(self):
        # データ属性を定義
        self.sound = "ニャー"
        self.legs = 4
        self.is_cat = True


# ねこのインスタンスを作成
my_cat = Cat()

# データ属性にアクセスして情報を表示
print("ねこの鳴き声:", my_cat.sound)
print("ねこの足の数:", my_cat.legs)
print("動物:", my_cat.is_cat)
