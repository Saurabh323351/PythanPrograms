""" This program actually gives the number of notes
and which note is required for a particular amount.
"""
from __future__ import print_function
from com.bridgelabz.util.utility import Utility

print("Enter Money")
MONEY_AMOUNT = Utility().get_int()
VENDING_RESULT = Utility.get_vending_machine_result(MONEY_AMOUNT)

for i in VENDING_RESULT:
    print(i+" "+str(VENDING_RESULT.get(i, -1)))
