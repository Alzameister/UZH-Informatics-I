#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def max_profit(prices):
	for el in prices:
		if el < 0:
			raise ValueError("Can't be negative")
		if type(el) != int:
			raise TypeError("Invalid Data Type within List")
	
	if type(prices) != list:
		raise TypeError ("Invalid Input Type")

	if not prices:
		raise IndexError ("Empty Price List")

	if len(prices) == 1:
		return 0
	
	if len(prices) > 1:
		for idx, price in enumerate(prices):
			if idx < len(prices)-1:
				if prices[idx] != prices[idx+1]:
					pass
				else:
					return 0
	

	max_profits = max(prices) - min(prices)
	return max_profits

i = max_profit([1])
print(i)