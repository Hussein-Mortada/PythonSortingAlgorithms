from comparisons.VolumeCompare import VolumeCompare
from comparisons.BaseAreaCompare import BaseAreaCompare
from modules.Shape import Shape


class MergeSort:
    def __init__(self, comparisonType):
        self.comparisonType = comparisonType
        self.vc = VolumeCompare()
        self.bc = BaseAreaCompare()

    def sort(self, array):
        self.merge_sort(array)

    def merge_sort(self, array):
        array_size = len(array)
        if array_size < 2:  # if array is empty or size is 1 it is already sorted
            return

        midpoint = array_size // 2
        left_half = array[:midpoint]
        right_half = array[midpoint:]

        self.merge_sort(left_half)  # recursively calls merge_sort on each half
        self.merge_sort(right_half)

        if self.comparisonType.lower() == "v":
            self.merge_volume(array, left_half, right_half)
        elif self.comparisonType.lower() == "b":
            self.merge_base_area(array, left_half, right_half)
        else:
            self.merge_height(array, left_half, right_half)

    def merge_height(self, array, left_half, right_half):
        left_size = len(left_half)
        right_size = len(right_half)
        left_iterator = right_iterator = array_iterator = 0

        while left_iterator < left_size and right_iterator < right_size:
            if left_half[left_iterator] >= right_half[right_iterator]:  # uses comparator to see which is bigger
                array[array_iterator] = left_half[left_iterator]
                left_iterator += 1
            else:
                array[array_iterator] = right_half[right_iterator]
                right_iterator += 1
            array_iterator += 1

        while left_iterator < left_size:
            array[array_iterator] = left_half[left_iterator]
            array_iterator += 1
            left_iterator += 1

        while right_iterator < right_size:
            array[array_iterator] = right_half[right_iterator]
            array_iterator += 1
            right_iterator += 1

    def merge_base_area(self, array, left_half, right_half):
        left_size = len(left_half)
        right_size = len(right_half)
        left_iterator = right_iterator = array_iterator = 0

        while left_iterator < left_size and right_iterator < right_size:
            if self.bc.compare(left_half[left_iterator], right_half[right_iterator]) >= 0:
                array[array_iterator] = left_half[left_iterator]
                left_iterator += 1
            else:
                array[array_iterator] = right_half[right_iterator]
                right_iterator += 1
            array_iterator += 1

        while left_iterator < left_size:
            array[array_iterator] = left_half[left_iterator]
            array_iterator += 1
            left_iterator += 1

        while right_iterator < right_size:
            array[array_iterator] = right_half[right_iterator]
            array_iterator += 1
            right_iterator += 1

    def merge_volume(self, array, left_half, right_half):
        left_size = len(left_half)
        right_size = len(right_half)
        left_iterator = right_iterator = array_iterator = 0

        while left_iterator < left_size and right_iterator < right_size:
            if self.vc.compare(left_half[left_iterator], right_half[right_iterator]) >= 0:
                array[array_iterator] = left_half[left_iterator]
                left_iterator += 1
            else:
                array[array_iterator] = right_half[right_iterator]
                right_iterator += 1
            array_iterator += 1

        while left_iterator < left_size:
            array[array_iterator] = left_half[left_iterator]
            array_iterator += 1
            left_iterator += 1

        while right_iterator < right_size:
            array[array_iterator] = right_half[right_iterator]
            array_iterator += 1
            right_iterator += 1
