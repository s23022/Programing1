def list_average(lst):
    try:
        # リストの合計を計算し、要素数で割って平均値を求める
        average = sum(lst) / len(lst)
        return average
    except ZeroDivisionError:
        return "リストは空です。"


# リストのテスト
my_list = [1.5, 2.5, 3.5, 4.5]
result = list_average(my_list)
print("平均値:", result)

empty_list = []
result = list_average(empty_list)
print("平均値:", result)
