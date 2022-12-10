from abc import ABC, abstractmethod


class GeometricObject(ABC):

    def __init__(self, color, filled):
        self._color = color
        self._filled = filled

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_filled(self):
        return self._filled

    def set_filled(self, filled):
        self._filled = filled
    
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass
