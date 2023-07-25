from modules import *

class VolumeCompare:
    def compare(self, shape1, shape2):
        return shape1.calc_volume() - shape2.calc_volume()

    def __call__(self, shape1, shape2):
        return self.compare(shape1, shape2)