#!/usr/bin/env python3
# add imports, if necessary
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES

class BankAccount:

    def __init__(self, currency="CHF"):
        if currency in EXCHANGE_RATES:
            self._currency = currency
            self._balance = 0
        else: raise Warning("Currency not available")

    def get_currency(self):
        return self._currency

    def get_balance(self):
        return self._balance
        
    def deposit(self, amount, currency="CHF"):
        if currency not in EXCHANGE_RATES:
            raise Warning("Currency not available")
        if amount < 0 or not isinstance(amount, (int, float)):
            raise Warning("Incorrect amount")

        if currency == self._currency:
            self._balance += amount
        else:
            self._balance += convert(amount, currency, self._currency)
        if self._balance < 0:
            raise Warning("Balance negative")
    
    def withdraw(self, amount, currency="CHF"):
        if currency not in EXCHANGE_RATES:
            raise Warning("Currency not available")
        if amount < 0 or not isinstance(amount, (int, float)):
            raise Warning("Incorrect amount")

        if currency == self._currency:
            self._balance -= amount
        else:
            self._balance -= convert(amount, currency, self._currency)
        if self._balance < 0:
            raise Warning("Balance negative")
        print("Hi")
        print("This is test_1")
        print("Test 2")