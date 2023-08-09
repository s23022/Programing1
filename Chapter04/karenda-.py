import datetime

def get_calendar(year, month):
    # 1日の曜日を取得
    first_day = datetime.date(year, month, 1)
    weekday = first_day.weekday()

    # 月の日数を取得
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    last_day = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
    days_in_month = last_day.day

    # カレンダーのヘッダーを表示
    header = f"{year}年{month}月"
    weekdays = "月 火 水 木 金 土 日"
    calendar_str = f"{header:^21}\n{weekdays}"

    # 月初の空白を追加（月曜日から始まるように）
    calendar_str += "\n" + "   " * weekday

    # 日付を配置
    day = 1
    while day <= days_in_month:
        if (weekday + day - 1) % 7 == 5:  # 土曜日の場合
            calendar_str += f"\033[34m{day:2d}\033[m "  # 青色で出力
        elif (weekday + day - 1) % 7 == 6:  # 日曜日の場合
            calendar_str += f"\033[31m{day:2d}\033[m "  # 赤色で出力
        else:
            calendar_str += f"{day:2d} "

        # 改行処理（日曜日の次は月曜日に改行）
        if (weekday + day) % 7 == 0:
            calendar_str += "\n"

        # 日付を1つ進める
        day += 1

    return calendar_str

# 現在の年月を取得
today = datetime.date.today()
year = today.year
month = today.month

# カレンダーを表示
calendar_output = get_calendar(year, month)
print(calendar_output)

