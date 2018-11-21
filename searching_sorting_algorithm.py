from com.bridgelabz.utility.Utility import Utility

utility_obj = Utility()

##########################################################Binary Search for Integer####################################
# print("Enter number of elements you want to put in list")
# list_int_size=utility_obj.get_int()
# print("Now enter all elements")
# store_user_value=[]
# for i in range(0,list_int_size):
#     store_user_value.append(utility_obj.get_int())
#
# print("Enter which element you are looking for")
# search_item=utility_obj.get_int()
# search_item_index=Utility.binary_search_for_int(store_user_value,search_item)
#
# if search_item_index!=-1:
#     print(str(store_user_value[search_item_index])+"  index => "+str(search_item_index))
#

 #######################################Binary Search for String#######################################################

print("Enter number of elements you want to put in list")

list_str_size=utility_obj.get_int()
store_user_value=[]
print("Now enter all elements")
for i in range(0,list_str_size):
    store_user_value.append(utility_obj.get_string())

print("Enter which element you are looking for")
search_item = utility_obj.get_string()
search_item_index = Utility.binary_search_for_string(store_user_value, search_item)

if search_item_index != -1:
    print(str(store_user_value[search_item_index]) + "  index => " + str(search_item_index))
