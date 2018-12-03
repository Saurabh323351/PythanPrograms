from com.bridgelabz.util.utility import Utility

utility_obj=Utility()

print("enter string to see all permutation  of it ")
string = utility_obj.get_string()
n = len(string)
a = list(string)
utility_obj.permute(a, 0, n-1)
