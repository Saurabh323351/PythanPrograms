from com.bridgelabz.util.utility import Utility
utility_obj=Utility()
print("Enter Number of values you want to enter")
no_of_values=utility_obj.get_int()
print("Enter values now")
store_values=[]
for i in range(0,no_of_values):
    value=utility_obj.get_int()
    store_values.append(value)

utility_obj.find_triplet(store_values)
