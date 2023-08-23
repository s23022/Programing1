# 辞書変数 name_age を作成
name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}

# dict_info 関数を定義


def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]
    except KeyError:
        return "key is not found"


# テスト
print(dict_info(name_age, "satou"))  # 25
print(dict_info(name_age, "yamada"))  # key is not found
