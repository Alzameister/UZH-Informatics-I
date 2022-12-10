#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        if not isinstance(gas_capacity, float) or gas_capacity < 0:
            gas_capacity = 0
            raise Warning("Invalid input")
        if not isinstance(gas_per_100km, float) or gas_per_100km < 0:
            gas_per_100km = 0
            raise Warning("Invalid input")
        if not isinstance(battery_size, float) or battery_size < 0:
            battery_size = 0
            raise Warning("Invalid input")
        if not isinstance(battery_range_km, float) or battery_range_km < 0:
            battery_range_km = 0
            raise Warning("Invalid input")
        
        self._gas_capacity = gas_capacity
        self._gas_per_100km = gas_per_100km
        self._battery_size = battery_size
        self._battery_range_km = battery_range_km
        self._charge = battery_size
        self._tank = gas_capacity

        self._electric_on = True

    def switch_to_combustion(self):
        self._electric_on = False

    def switch_to_electric(self):
        self._electric_on = True

    def get_remaining_range(self):
        range = 0
        range += ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)
        return range

    def drive(self, dist):
        if not isinstance(dist, float) or dist < 0:
            raise Warning("Invalid input")

        if self._electric_on:
            self._charge -= dist / self._battery_range_km * self._battery_size
            if self._charge <= 0:
                #Calculate driven distance
                dist_remaining = -(self.charge) / self._battery_size * self._battery_range_km
                dist = dist_remaining

                self._electric_on = False
                self._tank -= self._gas_per_100km / 100 * dist
        else:
            self._tank -= self._gas_per_100km / 100 * dist
            if self._tank <= 0:
                #Calculate driven distance
                dist_remaining = -(self._tank) / self._gas_per_100km * 100
                dist = dist_remaining

                self._electric_on = True
                self._charge -= dist / self._battery_range_km * self._battery_size
        
        if self._tank < 0:
            self._tank = 0
        if self._charge < 0:
            self._charge = 0

h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.switch_to_combustion()
h.drive(600.0) # depletes fuel, auto-switch
print(h.get_gas_tank_status()) # (0.0, 40.0)
print(h.get_battery_status()) # (20.0, 25.0)