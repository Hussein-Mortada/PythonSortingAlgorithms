from modules.Shape import Shape


class Pyramid(Shape):
    def __init__(self, height, side):
        super().__init__(height)
        self.side = side

    def get_side(self):
        return self.side

    def calc_volume(self):
        if self.volume < 0:
            self.volume = 1.0/3*self.calc_base_area()*self.get_height()
        return self.volume

    def calc_base_area(self):
        if self.base_area < 0:
            self.base_area = self.side*self.side
        return self.base_area

    def __str__(self):
        return f"Pyramid: Height: {self.get_height():.2f} Side: {self.side:.2f} Volume: {self.calc_volume():.2f} Base Area: {self.calc_base_area():.2f}"
