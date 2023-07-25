from comparisons.VolumeCompare import VolumeCompare
from comparisons.BaseAreaCompare import BaseAreaCompare
from modules.Shape import Shape


class BubbleSort:
    def __init__(self, comparisonType):
        self.comparisonType = comparisonType
        self.vc = VolumeCompare()
        self.bc = BaseAreaCompare()

    def sort(self, array):
        if self.comparisonType.lower() == "v":
            self.sort_by_volume(array)
        elif self.comparisonType.lower() == "b":
            self.sort_by_base_area(array)
        else:
            self.sort_by_height(array)

    def sort_by_height(self, array):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i].compare_to(array[j])>=0:
                    array[i], array[j] = array[j], array[i]

    def sort_by_base_area(self, array):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if self.bc(array[i], array[j]) <= 0:
                    array[i], array[j] = array[j], array[i]

    def sort_by_volume(self, array):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if self.vc(array[i], array[j]) <= 0:
                    array[i], array[j] = array[j], array[i]