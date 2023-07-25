from modules import *

class BaseAreaCompare:
    def compare(self, shape1, shape2):
        return shape1.calc_base_area() - shape2.calc_base_area()

    def __call__(self, shape1, shape2):
        return self.compare(shape1, shape2)
