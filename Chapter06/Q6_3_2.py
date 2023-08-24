class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


# 長方形のインスタンスを作成
rectangle = Rectangle(4, 5)

# 長方形の周の長さと面積を表示
print("長方形の周の長さ:", rectangle.calculate_perimeter())
print("長方形の面積:", rectangle.calculate_area())

# 正方形のインスタンスを作成
square = Square(3)

# 正方形の周の長さと面積を表示
print("正方形の周の長さ:", square.calculate_perimeter())
print("正方形の面積:", square.calculate_area())
