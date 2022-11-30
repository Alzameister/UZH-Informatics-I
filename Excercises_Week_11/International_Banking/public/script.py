#!/usr/bin/env python3
from bank_account import BankAccount

b = BankAccount("EUR")
b.deposit(10, "CHF")
print(b.get_balance())