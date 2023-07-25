import importlib
import os
import sys
import time
from modules.Cone import Cone
from modules.Cylinder import Cylinder
from modules.OctagonalPrism import OctagonalPrism
from modules.PentagonalPrism import PentagonalPrism
from modules.Pyramid import Pyramid
from modules.SquarePrism import SquarePrism
from modules.TriangularPrism import TriangularPrism
from sortingalgorithms.BubbleSort import BubbleSort
from sortingalgorithms.HeapSort import HeapSort
from sortingalgorithms.InsertionSort import InsertionSort
from sortingalgorithms.MergeSort import MergeSort
from sortingalgorithms.QuickSort import QuickSort
from sortingalgorithms.SelectionSort import SelectionSort


class Manager:
    def __init__(self):
        self.sortingMethod = None
        self.fileLocation = None
        self.comparisonType = None
        self.fileReadTime = None
        self.shapes = None

    def start(self):
        self.parseInputs()
        self.fillArray()
        self.callSort(self.sortingMethod,self.comparisonType)

    def parseInputs(self):
        try:
            self.fileLocation = input("Please enter the file location for the shapes: ")
            self.comparisonType = input(
                "Please enter the comparison type. b for base area compare, v for volume compare, or h for height comparison: ")
            self.sortingMethod = input(
                "Please enter the sorting algorithm. Enter 'b' for bubble, 's' for selection, 'i' for insertion, 'm' for merge, 'q' for quick, or 'z' for heap sort: ")

            if not self.fileLocation or not self.comparisonType or not self.sortingMethod:
                print("Error: Missing command line arguments. Please enter all values.")
                sys.exit(0)

            if self.comparisonType.lower() not in ['b', 'v', 'h']:
                print("Error: Please enter a valid comparison type. Use 'b', 'v', or 'h'.")
                sys.exit(0)

            if self.sortingMethod.lower() not in ['b', 's', 'i', 'm', 'q', 'z']:
                print("Error: Please enter a valid sorting algorithm. Use 'b', 's', 'i', 'm', 'q', or 'z'.")
                sys.exit(0)

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

    def fillArray(self):
        try:
            with open(self.fileLocation, 'r') as file:
                line = file.readline().strip('\n')
                shape_info_list = line.split()

                arraySize = int(shape_info_list[0])
                print(arraySize)

                shapes = [None] * arraySize
                start_time = time.time()
                currentValueInArray = 0
                line = file.readline()
                shape_info_list = line.split()
                for i in range(0, len(shape_info_list), 3):
                    shape_name = shape_info_list[i]
                    measurement1 = float(shape_info_list[i + 1])
                    measurement2 = float(shape_info_list[i + 2])

                    module_name = "modules." + shape_name
                    module = importlib.import_module(module_name)
                    cls = getattr(module, shape_name)
                    shape = cls(measurement1, measurement2)
                    shapes[currentValueInArray] = shape
                    currentValueInArray += 1

            end_time = time.time()
            self.shapes = shapes
            self.fileReadTime = int((end_time - start_time) * 1000)
        except FileNotFoundError:
            print("Error: File not found. Please enter a valid file path.")
        except (AttributeError, ImportError):
            print("Error: Class not found or incorrect import. Please check the class name and import statement.")
        except Exception as e:
            print(f"Error: {e}")

    def callSort(self, sortingAlgorithm, comparisonType):
        start = None
        end = None

        if sortingAlgorithm.lower() == "b":
            bs = BubbleSort(comparisonType)
            start = time.time()
            bs.sort(self.shapes)
            end = time.time()
        elif sortingAlgorithm.lower() == "s":
            ss = SelectionSort(comparisonType)
            start = time.time()
            ss.sort(self.shapes)
            end = time.time()
        elif sortingAlgorithm.lower() == "i":
            is_ = InsertionSort(comparisonType)
            start = time.time()
            is_.sort(self.shapes)
            end = time.time()
        elif sortingAlgorithm.lower() == "m":
            ms = MergeSort(comparisonType)
            start = time.time()
            ms.sort(self.shapes)
            end = time.time()
        elif sortingAlgorithm.lower() == "q":
            qs = QuickSort(comparisonType)
            start = time.time()
            qs.sort(self.shapes)
            end = time.time()
        elif sortingAlgorithm.lower() == "z":
            hs = HeapSort(comparisonType)
            start = time.time()
            hs.sort(self.shapes)
            end = time.time()
        else:
            print(
                "Error: Invalid sort type. Please enter 'b' for bubble, 's' for selection, 'i' for insertion, 'm' for merge, 'q' for quick, or 'z' for your choice of sorting algorithm.")
            sys.exit(1)

        self.printSortedArray()
        print("Time to read file: {} Milliseconds".format(self.fileReadTime))
        print("Time to complete {} Sort: {} Milliseconds".format(sortingAlgorithm.capitalize(), (end - start) * 1000))
        print()

    def printSortedArray(self):
        for i in range(0, len(self.shapes), 1000):
            if (i + 1000) > len(self.shapes):  # Printing the last value of the array
                print(self.shapes[-1])
                break
            print(self.shapes[i])