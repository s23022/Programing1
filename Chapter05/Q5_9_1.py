mountain_in_japan = {"fuji": 3776, "kitadake": 3193, "okuhodakadaka": 3190, "dummy": 0}

# 標高の逆順にソート
sorted_mountain = dict(
    sorted(mountain_in_japan.items(), key=lambda x: x[1], reverse=True)
)

print(sorted_mountain)
