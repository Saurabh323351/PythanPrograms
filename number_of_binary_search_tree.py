from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *

utility_obj=Utility()
binary_obj=BinaryTreeNode()
print('Enter How many nodes you want to insert into list')
nodes_count=utility_obj.get_int()

nodes_list=[]
print('Now Enter all test cases')
for i in range(0,nodes_count):
    nodes_list.append(utility_obj.get_int())


binary_obj.count_binary_search_tree(nodes_list)
