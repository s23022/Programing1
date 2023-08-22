# 空のキューを作成
queue = []

# 要素1をキューに追加
queue.append(1)

# 要素2をキューに追加
queue.append(2)

# キューの先頭から要素を2回取得
element1 = queue.pop(0)
element2 = queue.pop(0)

# 取得した要素を表示
print("取得した要素1:", element1)
print("取得した要素2:", element2)
