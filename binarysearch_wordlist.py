from com.bridgelabz.utility.Utility import Utility

utility_obj=Utility()

list=Utility.binarysearch_wordlist()
print("These are the list of items we have in our list\n")
for i in list:
    print(i,end=" ")

print("\n\nEnter word you are looking for")
search_item=Utility().get_string()
search_item_index=Utility.binary_search_for_string(list,search_item)
if search_item_index != -1:
    print(str(list[search_item_index]) + "  index => " + str(search_item_index))