import math


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius  # 円柱の半径
        self.height = height  # 円柱の高さ

    def calculate_surface_area(self):
        # 表面積を計算
        # 2πr² + 2πrh
        return 2 * math.pi * self.radius**2 + 2 * math.pi * self.radius * self.height

    def calculate_volume(self):
        # 体積を計算
        # πr²h
        return math.pi * self.radius**2 * self.height


# 円柱のインスタンスを作成
cylinder1 = Cylinder(5.0, 10.0)  # 半径5.0、高さ10.0の円柱
cylinder2 = Cylinder(3.0, 7.5)  # 半径3.0、高さ7.5の円柱

# 表面積と体積を計算して表示
print("円柱1の表面積:", cylinder1.calculate_surface_area())
print("円柱1の体積:", cylinder1.calculate_volume())

print("円柱2の表面積:", cylinder2.calculate_surface_area())
print("円柱2の体積:", cylinder2.calculate_volume())
