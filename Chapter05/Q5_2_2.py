list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
[x if x % 2 == 0 else None for x in list1]
# 出力結果　[None,2,None,4,None,6,None,8,None]
