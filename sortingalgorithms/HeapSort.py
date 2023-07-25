from comparisons.VolumeCompare import VolumeCompare
from comparisons.BaseAreaCompare import BaseAreaCompare
from modules.Shape import Shape


class HeapSort:
    def __init__(self, comparisonType):
        self.comparisonType = comparisonType
        self.vc = VolumeCompare()
        self.bc = BaseAreaCompare()

    def sort(self, array):
        self.heap_sort(array)

    def heap_sort(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(array, n, i)

        for i in range(n - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            self.heapify(array, i, 0)

    def heapify(self, array, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if self.comparisonType.lower() == "v":
            if l < n and self.vc.compare(array[l], array[largest]) <= 0:
                largest = l

            if r < n and self.vc.compare(array[r], array[largest]) <= 0:
                largest = r

        elif self.comparisonType.lower() == "b":
            if l < n and self.bc.compare(array[l], array[largest]) <= 0:
                largest = l

            if r < n and self.bc.compare(array[r], array[largest]) <= 0:
                largest = r

        else:
            if l < n and array[l] <= array[largest]:
                largest = l

            if r < n and array[r] <= array[largest]:
                largest = r

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.heapify(array, n, largest)
