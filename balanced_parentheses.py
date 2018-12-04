"""Balanced Parentheses Program

This program is used to check whether user given arithmetic expression is balanced or not

Example:
    Balaced Expression :: {{a+b}*[a-b]}

    Unbalanced Expression:: {{a+b}*[a-b]

Author:
    Saurabh <singh.saurabh3333@gmail.com>

Since:
    20 Nov,2018

"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def balance_parentheses():
    """
    This method is used as runner balanced_parentheses(string) method

    :return:  nothing
    """
    utility_obj = Utility()
    stack = Stack()
    print("Enter Expression to check for balanced Parentheses")
    try:
        string = utility_obj.get_string()
    except Exception as e:
        print(e)
        print("Enter String")

    stack.balanced_parentheses(string)


if __name__ == "__main__":
    balance_parentheses()
