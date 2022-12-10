from geometric_object import GeometricObject


class Cone(GeometricObject):

    def __init__(self, radius, vertical_height, slant_height, color, filled):
        super().__init__(color, filled)
        self.__pi = 3.14
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = slant_height

    def get_radius(self):
        return self.__radius

    def get_vertical_height(self):
        return self.__vertical_height

    def get_slant_height(self):
        return self.__slant_height

    def get_area(self):
        area = round((self.__pi * self.__radius**2) + (self.__pi * self.__radius * self.__slant_height), 2)
        return area

    def get_volume(self):
        volume = round(self.__radius ** 2 * self.__pi * self.__vertical_height * (1/3), 2)
        return volume
