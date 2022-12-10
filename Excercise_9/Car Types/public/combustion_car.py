#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not isinstance(gas_capacity, float) or gas_capacity < 0:
            gas_capacity = 0
            raise Warning("Invalid input")
        if not isinstance(gas_per_100km, float) or gas_per_100km < 0:
            gas_per_100km = 0
            raise Warning("Invalid input")

        self._gas_capacity = gas_capacity
        self._gas_per_100km = gas_per_100km
        self._tank = gas_capacity

    def fuel(self, f):
        if f >= 0:
            self._tank += f
        else:
            f = 0
            raise Warning("Invalid input")
        if self._tank > self._gas_capacity:
            raise Warning("Overfueled!")

    def get_gas_tank_status(self):
        return self._tank, self._gas_capacity

    def get_remaining_range(self):
        #remaining range = remaining gas / gas per * 100
        return self._tank / self._gas_per_100km * 100

    def drive(self, dist):
        if not isinstance(dist, float) or dist < 0:
            raise Warning("Invalid input")

        #gas usage = gas per 100km / 100 * dist
        self._tank -= self._gas_per_100km / 100 * dist
        print(self._tank)
        if self._tank <= 0:
            raise Warning("Tank empty!")

c = CombustionCar(40.0, 8.0)
print(c.get_remaining_range())
c.get_remaining_range() # 500
c.drive(25.0)
c.get_gas_tank_status() # (38.0, 40.0)
c.drive(490.0) # fuel is depleted, Warning raised