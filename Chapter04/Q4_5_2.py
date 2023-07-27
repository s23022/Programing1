coordinates_str = ["1.0 2.2 3.5", "2.1 3.2 5.5", "1.2 1.3 2.2", "2.1 3.1 4.5"]


def convert_to_coordinates(coord_str):
    return list(map(float, coord_str.split()))


coordinates_list = list(map(convert_to_coordinates, coordinates_str))
print(coordinates_list)
