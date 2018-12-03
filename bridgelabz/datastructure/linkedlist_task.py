"""
Read the Text from a file, split it into words and arrange it as Linked List.

Take a user input to search a Word in the List.
If the Word is not found then add it to the list,
and if it found then remove the word from the List.
In the end save the list into a file

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
    print(len(list))
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
    except:
        print("Enter string only")
    print(obj.search_item(data))

    print("The updated file content are as follows")
    obj.file_update(data)


if __name__ == '__main__':
    linkedlist_task()
