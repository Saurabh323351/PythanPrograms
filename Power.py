from com.bridgelabz.utility.Utility import Utility


utility_obj = Utility()
print("Enter limit")
limit=utility_obj.get_int()

l=utility_obj.power(limit)
for i in l:
    print(i)