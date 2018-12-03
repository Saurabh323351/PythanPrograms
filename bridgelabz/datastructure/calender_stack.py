"""
Take the month and year from user and print the corresponding calender .

here calender should be created using stack
"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def calender_runner():
    """
    this method is used as runner for calender_stack(month, year) method

    :return:  nothing
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

    logic_obj.calender_stack(month, year)


if __name__ == "__main__":
    calender_runner()
