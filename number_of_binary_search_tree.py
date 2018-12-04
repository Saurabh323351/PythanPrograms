"""Possible Number of Binary Search Tree Program

This program is used to generate number of possible binary search tree in given number of test cases

Author:
    Saurabh<singh.saurabh3333@gmail.com>

Since:
    28 Nov,2018
"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def binary_count_runner():
    """
    This method act as runner for count_binary_search_tree(nodes_list) method

    :return: this won't return anything
    """
    utility_obj = Utility()
    binary_obj = BinaryTreeNode()
    print('Enter How many nodes you want to insert into list')
    try:
        nodes_count = utility_obj.get_int()
    except Exception as e:
        print(e)
        print("Enter Number of nodes in integer only")
    nodes_list = []
    print('Now Enter all test cases')
    for i in range(0, nodes_count):
        nodes_list.append(utility_obj.get_int())

    result = binary_obj.count_binary_search_tree(nodes_list)
    print("No of Binary tree possible in each test case is as follows")
    for i in result:
        print(i)


if __name__ == "__main__":
    binary_count_runner()
