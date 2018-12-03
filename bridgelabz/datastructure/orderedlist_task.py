"""
Read a List of Numbers from a file and arrange it ascending Order in a Linked List.
Take user input for a number, if found then pop the number out of the list
else insert the number in appropriate position

"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def orderedlist_task():
    """
    This method is used to read content of file.

    this method also append data into orderedList to perform operation on it
    this method also acts as runner for various method

    :return:nothing
    """
    utility_obj = Utility()
    orderedlist_obj = OrderedList()

    file = open("../util/LinkedList_File", "r+")

    list = file.readlines()
    file_string = list[0]

    list = file_string.split()

    for i in range(0, len(list)):
        orderedlist_obj.add(list[i].strip())
    file.close()

    print("These are the data that we have in our File")

    file = open("../util/LinkedList_File", "r+")

    list = file.readlines()
    list = list[0]
    print(list)
    file.close()
    print("Enter data you are looking for")
    try:
        data = utility_obj.get_string()
    except:
        print('Enter data in string only')
    print(orderedlist_obj.search_item(data))

    print("The updated file content are as follows")
    orderedlist_obj.file_update(data)


if __name__ == '__main__':
    orderedlist_task()
