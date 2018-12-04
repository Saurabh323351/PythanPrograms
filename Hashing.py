"""Hashing Program

This program is used to store user data into hashtable efficiently using hash function
and user can search their data in O(1) time complexity and
if data is found then that data will be removed and saves into file
and if data is not found then that data will be added to the hashtable and saves into file
At last user can see the updated content of file

Author:
    Saurabh<singh.saurabh3333@gmail.com>

Since:
    23,Nov 2018

"""

from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *


def hashing_runner():
    """
    This method acts as runner
    :return: nothing
    """
    utility_obj = Utility()
    hash_obj = HashTable()

    print('These are the Numbers in our File')
    file = open("../util/HashTable File", "r")
    print(file.readline())

    print('Now enter the Number you are looking for')
    try:
        number = utility_obj.get_int()
    except Exception as e:
        print(e)
        print("Enter Number only")
    hash_obj.insert()
    print(hash_obj.search(number))

    print('Now Updated File Content are as Follows')
    hash_obj.file_update(number)


if __name__ == "__main__":
    hashing_runner()
  