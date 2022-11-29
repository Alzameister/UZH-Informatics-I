#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if battery_size < 0 or not isinstance(battery_size, float):
            battery_size = 0
            raise Warning("Invalid input")
        if battery_range_km < 0 or not isinstance(battery_range_km, float):
            battery_range_km = 0
            raise Warning("Invalid input")

        self._battery_size = battery_size
        self._battery_range_km = battery_range_km
        self._charge = battery_size

    def charge(self, kwh):
        if kwh >= 0:
            self._charge += kwh
        else:
            kwh = 0
            raise Warning("Invalid input")
        if self._charge > self._battery_size:
            raise Warning("Overcharged!")

    def get_battery_status(self):
        return self._charge, self._battery_size

    def get_remaining_range(self):
        #Remaining range = charge / battery size * battery range
        return self.charge / self._battery_size * self._battery_range_km

    def drive(self, dist):
        if dist < 0 or not isinstance(dist, float):
            raise Warning("Invalid input")

        #charge_usage = dist / battery range * battery size
        self._charge -= dist / self._battery_range_km * self._battery_size
        if self._charge <= 0:
            raise Warning("Tank empty!")


