from datetime import datetime, timedelta


def classify_date(day_offset=0):
    today = datetime.now().date()

    target_date = today + timedelta(days=day_offset)

    if target_date < today:
        return "昨日"
    elif target_date == today:
        return "今日"
    elif target_date == today + timedelta(days=1):
        return "明日"
    else:
        return "今日より一日を超えて離れた日"


print(classify_date(3))
