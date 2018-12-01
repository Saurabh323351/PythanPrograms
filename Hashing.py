from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *

utility_obj=Utility()
hash_obj=HashTable()


print('These are the Numbers in our File')
file=open("../util/HashTable File", "r")
print(file.readline())

print('Now enter the Number you are looking for')
number=utility_obj.get_int()
hash_obj.insert()
print(hash_obj.search(number))

print('Now Updated File Content are as Follows')
# hash_obj.file_update(number)
