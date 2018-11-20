from com.bridgelabz.utility.Utility import Utility


utility_obj = Utility()
print("Enter Number of Coupans you want")
no_of_coupans=utility_obj.get_int()
random_number_count,store_coupans = utility_obj.coupan_generator(no_of_coupans)
print("Number of Random Number Needed to Generate given number of coupans =>"+str(random_number_count))
print("The Distinct Coupans are as follows")
for i in store_coupans:
    print(i)
