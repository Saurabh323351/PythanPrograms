"""
Create a Slot of 10 to store Chain of Numbers that belong to each Slot to efficiently search
a number from a given set of number

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
    except:
        print("Enter Number only")
    hash_obj.insert()
    print(hash_obj.search(number))

    print('Now Updated File Content are as Follows')
    hash_obj.file_update(number)


if __name__ == "__main__":
    hashing_runner()
  