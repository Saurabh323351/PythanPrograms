"""Calender using Queue Program

This program is used to take month and year from user and print corresponding Calender using queue

Example:
    Enter Month:: 11
    Enter Year :: 2018

    Your Calender is Ready

    S  M  T  W  Th F  S
                1  2  3
    4  5  6  7  8  9  10
    11 12 13 14 15 16 17
    18 19 20 21 22 23 24
    25 26 27 28 29 30

Author:
    Saurabh<singh.saurabh3333@gmail.com>

Since:
    22 Nov,2018
"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def calender_runner():
    """
    This method act as runner for calender_queue(month, year) method
    :return:This method won't return anything
    """
    utility_obj = Utility()

    logic_obj = Logic()

    print('Enter Month')
    try:
        month = utility_obj.get_int()
    except Exception as e:
        print(e)
        print("Enter integer only ")
    print('Enter Year')
    try:
        year = utility_obj.get_int()
    except Exception as e:
        print(e)
        print("Enter integer only")

    logic_obj.calender_queue(month, year)


if __name__ == "__main__":
    calender_runner()
