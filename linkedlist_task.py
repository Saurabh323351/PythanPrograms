"""LinkedList File Program

This program is used to take input from file and user can see the content of file
then user can search for data that he is looking for .if the user data is found then
that data will be removed from  LinkedList and saves into file and vice versa
and at last user can see the updated content of file

Author:
    Saurabh<singh.saurabh3333@gmail.com>

Since:
    25 Nov,2018
"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def linkedlist_task():
    """
    This method is used to read content of file.

    this method also append data into orderedList to perform operation on it
    this method also acts as runner for various method

    :return:nothing
    """
    utility_obj = Utility()
    obj = LinkedList()

    file = open("../util/LinkedList_File", "r+")

    list = file.readlines()

    file_string = list[0]

    list = file_string.split()

    for i in range(0, len(list)):
        obj.append(list[i].strip())
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
    except Exception as e:
        print(e)
        print("Enter string only")
    print(obj.search_item(data))

    print("The updated file content are as follows")
    obj.file_update(data)


if __name__ == '__main__':
    linkedlist_task()
