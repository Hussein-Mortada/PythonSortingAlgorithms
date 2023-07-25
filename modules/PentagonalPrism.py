import math
from modules.Shape import Shape


class PentagonalPrism(Shape):
    def __init__(self, height, side):
        super().__init__(height)
        self.side = side

    def get_side(self):
        return self.side

    def calc_volume(self):
        if self.volume < 0:
            self.volume = self.calc_base_area() * self.get_height()
        return self.volume

    def calc_base_area(self):
        if self.base_area < 0:
            self.base_area = (5.0 * self.side * self.side * math.tan(math.radians(54))) / 4.0
        return self.base_area

    def __str__(self):
        return f"PentagonalPrism: Height: {self.get_height():.2f} Side: {self.side:.2f} Volume: {self.calc_volume():.2f} Base Area: {self.calc_base_area():.2f}"
