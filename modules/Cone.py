from math import pi
from modules.Shape import Shape


class Cone(Shape):
    def __init__(self, height, radius):
        super().__init__(height)
        self.radius = radius


    def get_radius(self):
        return self.radius

    def calc_volume(self):
        if self.volume < 0:
            self.volume = self.calc_base_area() * self.get_height() * 1.0 / 3
        return self.volume

    def calc_base_area(self):
        if self.base_area < 0:
            self.base_area = pi * self.radius * self.radius
        return self.base_area

    def __str__(self):
        return f"Cone: Height: {self.get_height():.2f} Radius: {self.radius:.2f} Volume: {self.calc_volume():.2f} Base Area: {self.calc_base_area():.2f}"
