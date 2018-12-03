"""
Take an Arithmetic Expression where parentheses are used to order the performance of operations.
 Ensure parentheses must appear in a balanced fashion.
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
    except:
        print("Enter String")

    stack.balanced_parentheses(string)


if __name__ == "__main__":
    balance_parentheses()
