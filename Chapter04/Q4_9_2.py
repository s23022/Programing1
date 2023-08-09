import os  # osモジュールをインポート
import sys  # sysモジュールをインポート

MAX = 2  # 定数MAXを定義

# デフォルトのエンコーディングを表示
print(sys.getdefaultencoding())

# 現在の作業ディレクトリのベース名を表示
print(os.path.basename(os.getcwd()))

# 0から2までの範囲でループ
for i in range(3):
    print(i, end=" ")  # iを表示して改行しないで続ける

    # もしMAXがiより大きければ
    if MAX > i:
        print(MAX)  # MAXの値を表示
    else:
        print("#")  # そうでなければ"#"を表示
