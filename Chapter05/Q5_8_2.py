data = [
    ["01", "0001", "male", "yamada", "tarou", 25, "tokyo"],
    ["01", "0002", "male", "satou", "takesi", 27, "kanagawa"],
    ["01", "0003", "female", "tanaka", "yuko", 22, "newjersey"],
    ["02", "0001", "male", "smith", "mika", 22, "newjersey"],
    ["02", "0002", "male", "turnet", "tom", 27, "kansas"],
    ["02", "0003", "male", "jackson", "david", 22, "fiorida"],
]
data

member_information = {}

for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_information[key] = info

print("number", "information", sep="\t")
for key, info in member_information.items():
    print(key, info)
