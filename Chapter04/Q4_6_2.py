students_data = [
    (1, 165, 55),
    (2, 180, 70),
    (3, 155, 45),
    (10, 175, 60),
]

sorted_by_height = sorted(students_data, key=lambda x: (x[1], str(x[0]) + "n"))

sorted_by_weight = sorted(students_data, key=lambda x: (x[2], str(x[0]) + "n"))
