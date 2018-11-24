from com.bridgelabz.util.utility import Utility
from timeit import default_timer
import time
#from time import clock_gettime_ns
utility_obj = Utility()
execution_time={}

execution_time["Method Name"]="Execution Time"
print("1.Binary Search for Integer\n2.Binary_search_for_string\n3.insertionsort_for_integer\n4.Insertion sort for string\n5.bubblesort_for_integer\n6.bubblesort_for_string")
choice=utility_obj.get_int()


##########################################################Binary Search for Integer####################################

if(choice==1):
    print("Enter number of elements you want to put in list")
    list_int_size=utility_obj.get_int()
    print("Now enter all elements")
    store_user_value=[]
    for i in range(0,list_int_size):
        store_user_value.append(utility_obj.get_int())

    print("Enter which element you are looking for")
    search_item=utility_obj.get_int()

    #start_time=default_timer()
    start_time=(time.time()*1000*1000)
    search_item_index=Utility.binary_search_for_int(store_user_value, search_item)
    #end_time=default_timer()
    end_time=(time.time()*1000*1000)
    binary_search_for_int=0
    execution_time[binary_search_for_int]=(end_time-start_time)
    print(execution_time.get(binary_search_for_int))

    if search_item_index!=-1:
        print(str(store_user_value[search_item_index])+"  index => "+str(search_item_index))


 #######################################Binary Search for String#######################################################



if(choice==2):
    print("Enter number of elements you want to put in list")

    list_str_size=utility_obj.get_int()
    store_user_value=[]
    print("Now enter all elements")
    for i in range(0,list_str_size):
        store_user_value.append(utility_obj.get_string())

    print("Enter which element you are looking for")
    search_item = utility_obj.get_string()

    start_time = (time.time() * 1000 * 1000)
    search_item_index = Utility.binary_search_for_string(store_user_value, search_item)
    end_time = (time.time() * 1000 * 1000)
    binary_search_for_string=''
    execution_time[binary_search_for_string]=(end_time-start_time)
    if search_item_index != -1:
        print(str(store_user_value[search_item_index]) + "  index => " + str(search_item_index))

#######################################Insertion sort for Integer######################################################



if(choice==3):
    print("Enter number of elements you want to put in list")
    list_int_size=utility_obj.get_int()
    print("Now enter all elements")
    store_user_value=[]
    for i in range(0,list_int_size):
        store_user_value.append(utility_obj.get_int())

    start_time = (time.time() * 1000 * 1000)
    sorted_list=Utility.insertionsort_for_integer(store_user_value)
    end_time = (time.time() * 1000 * 1000)

    insertionsort_for_integer=0
    execution_time[insertionsort_for_integer] = (end_time - start_time)
    for i in sorted_list:
        print(i, end=" ")



######################################Insertion sort for string#######################################################


if(choice==4):
    print("Enter number of elements you want to put in list")

    list_str_size=utility_obj.get_int()
    store_user_value=[]
    print("Now enter all elements")
    for i in range(0,list_str_size):
        store_user_value.append(utility_obj.get_string())

    start_time = (time.time() * 1000 * 1000)
    sorted_str_list=Utility.insertionsort_for_string(store_user_value)
    end_time = (time.time() * 1000 * 1000)
    insertionsort_for_string=''
    execution_time[insertionsort_for_string] = (end_time - start_time)
    for i in sorted_str_list:
        print(i,end=" ")


#####################################bubblesort_for_integer###########################################################


if(choice==5):
    print("Enter number of elements you want to put in list")
    list_int_size = utility_obj.get_int()
    print("Now enter all elements")
    store_user_value = []
    for i in range(0, list_int_size):
        store_user_value.append(utility_obj.get_int())

    start_time = (time.time() * 1000 * 1000)
    sorted_list = Utility.bubblesort_for_integer(store_user_value)
    end_time = (time.time() * 1000 * 1000)
    bubblesort_for_integer=0
    execution_time[bubblesort_for_integer] = (end_time - start_time)
    for i in sorted_list:
        print(i,end=" ")


######################################bubblesort_for_string############################################################



if(choice==6):
    print("Enter number of elements you want to put in list")

    list_str_size=utility_obj.get_int()
    store_user_value=[]
    print("Now enter all elements")
    for i in range(0,list_str_size):
        store_user_value.append(utility_obj.get_string())

    start_time = (time.time() * 1000 * 1000)
    sorted_str_list=Utility.bubblesort_for_string(store_user_value)
    end_time = (time.time() * 1000 * 1000)
    bubblesort_for_string=''
    execution_time[bubblesort_for_string] = (end_time - start_time)

    for i in sorted_str_list:
        print(i,end=" ")
