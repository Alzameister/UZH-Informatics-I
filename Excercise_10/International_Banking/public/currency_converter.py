#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES

def convert(amount, from_currency, to_currency):
    if not isinstance(amount, (int, float)):
        raise Warning("Amount not integer")
    if not isinstance(from_currency, str) or not isinstance(to_currency, str):
        raise Warning("Currency must be string")
    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        raise Warning("Invalid currency")

    if to_currency in EXCHANGE_RATES[from_currency]:
        exchange_rate = EXCHANGE_RATES[from_currency][to_currency]
        amount = amount * exchange_rate
    else:
        exchange_rate = 1/EXCHANGE_RATES[to_currency][from_currency]
        amount = amount * exchange_rate

    return amount