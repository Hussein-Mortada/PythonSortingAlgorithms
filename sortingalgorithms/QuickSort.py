from comparisons.VolumeCompare import VolumeCompare
from comparisons.BaseAreaCompare import BaseAreaCompare
from modules.Shape import Shape
import random


class QuickSort:
    def __init__(self, comparisonType):
        self.comparisonType = comparisonType
        self.vc = VolumeCompare()
        self.bc = BaseAreaCompare()

    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)

    def quick_sort(self, array, low, high):
        if low >= high:  # validates the array first
            return

        pivot_index = random.randint(low, high)  # random pivot index
        pivot = array[pivot_index]  # pivot to use
        self.swap(array, pivot_index, high)  # puts the pivot to the end of the array

        left_p = self.partition(array, low, high, pivot)

        self.quick_sort(array, low, left_p - 1)  # recursively calls quicksort on both halves
        self.quick_sort(array, left_p + 1, high)

    def partition(self, array, low, high, pivot):
        left_p = low  # left of the pivot starting at the low
        right_p = high  # right of pivot starting at high

        while left_p < right_p:  # loops until all elements sorted to left and right of pivot correctly
            if self.comparisonType.lower() == "v":  # volume compare
                while self.vc.compare(array[left_p], pivot) >= 0 and left_p < right_p:  # loops to find an element where smaller than pivot
                    left_p += 1

                while self.vc.compare(array[right_p], pivot) <= 0 and left_p < right_p:  # move right pointer until larger value found
                    right_p -= 1

            elif self.comparisonType.lower() == "b":  # base area compare
                while self.bc.compare(array[left_p], pivot) >= 0 and left_p < right_p:
                    left_p += 1

                while self.bc.compare(array[right_p], pivot) <= 0 and left_p < right_p:
                    right_p -= 1

            else:  # height compare
                while array[left_p].compare_to(pivot) >= 0 and left_p < right_p:
                    left_p += 1

                while array[right_p].compare_to(pivot) <= 0 and left_p < right_p:
                    right_p -= 1

            self.swap(array, left_p, right_p)  # swaps the left and right pivot

        self.swap(array, left_p, high)  # swaps left pivot and the high point
        return left_p  # returns the left pivot index

    def swap(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp
