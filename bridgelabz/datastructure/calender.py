"""
Take the month and year from user and print the corresponding calender .
"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def calender_runner():
    """
    This method act as runner for calender_queue(month, year)
    :return: nothing
    """
    utility_obj = Utility()

    logic_obj = Logic()

    print('Enter Month')
    try:
        month = utility_obj.get_int()
    except:
        print("Enter integer only ")
    print('Enter Year')
    try:
        year = utility_obj.get_int()
    except:
        print("Enter integer only")
    logic_obj.calender(month, year)


if __name__ == "__main__":
    calender_runner()
   