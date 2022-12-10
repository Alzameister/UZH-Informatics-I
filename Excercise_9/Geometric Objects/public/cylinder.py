from geometric_object import GeometricObject


class Cylinder(GeometricObject):

    def __init__(self, radius, height, color, filled):
        super().__init__(color, filled)
        self.__radius = radius
        self.__height = height
        self.__pi = 3.14

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        return round(2*self.__pi*self.__radius**2 + 2*self.__pi*self.__radius*self.__height, 2)

    def get_volume(self):
        return round(self.__pi * self.__radius**2 * self.__height, 2)
