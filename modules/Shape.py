from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, height):
        self.height = height
        self.base_area = -1
        self.volume = -1

    def get_height(self):
        return self.height

    @abstractmethod
    def calc_volume(self):
        pass

    @abstractmethod
    def calc_base_area(self):
        pass

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height

    def compare_to(self, other):
        if not isinstance(other, Shape):
            raise ValueError("Comparison is only supported with other Shape objects.")

        return self.height - other.height
