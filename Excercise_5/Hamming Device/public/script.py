#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

from queue import Empty

def calculate_hamming_dist(string_1, string_2):
    d = 0
    for char_1, char_2 in zip(string_1, string_2):
        if char_1 is not char_2:
            d += 1
    return d

def hamming_dist(signal_1, signal_2):
    invalid_strings = []
    #Return empty signal if datasets have different lengths and/or are empty
    if len(signal_1["data"]) is not len(signal_2):
        return "Empty signal on at least one of the sensors"

    #Extract data strings from sensors and compare
    for data_string_1, data_string_2 in zip(signal_1["data"], signal_2):
        if len(data_string_1) is not len(data_string_2):
            return "Sensor defect detected"
        else:
            d = calculate_hamming_dist(data_string_1, data_string_2)
            if d > 0:
                invalid_strings.append((data_string_1, data_string_2, d))

    return invalid_strings


# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
