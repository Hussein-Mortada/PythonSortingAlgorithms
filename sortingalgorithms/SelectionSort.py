from comparisons.VolumeCompare import VolumeCompare
from comparisons.BaseAreaCompare import BaseAreaCompare
from modules.Shape import Shape


class SelectionSort:
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
        for i in range(len(array) - 1):
            max_element_index = i
            for j in range(i + 1, len(array)):
                if array[max_element_index].compare_to(array[j]) <= 0:
                    max_element_index = j

            if max_element_index != i:
                array[i], array[max_element_index] = array[max_element_index], array[i]

    def sort_by_base_area(self, array):
        for i in range(len(array) - 1):
            max_element_index = i
            for j in range(i + 1, len(array)):
                if self.bc.compare(array[max_element_index], array[j]) <= 0:
                    max_element_index = j

            if max_element_index != i:
                array[i], array[max_element_index] = array[max_element_index], array[i]

    def sort_by_volume(self, array):
        for i in range(len(array) - 1):
            max_element_index = i
            for j in range(i + 1, len(array)):
                if self.vc.compare(array[max_element_index], array[j]) <= 0:
                    max_element_index = j

            if max_element_index != i:
                array[i], array[max_element_index] = array[max_element_index], array[i]
