from com.bridgelabz.util.utility import Utility

utility_obj=Utility()
print("Enter the size of list")
list_size=utility_obj.get_int()
print("Enter values")

user_list=[]
for i in range(0,list_size):
    user_list.append(utility_obj.get_int())

sorted_values=utility_obj.mergesort(user_list)
for i in sorted_values:
    print(i,end=" ")