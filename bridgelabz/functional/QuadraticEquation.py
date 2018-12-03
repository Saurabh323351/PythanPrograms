from com.bridgelabz.util.utility import Utility
utility_obj=Utility()
print("Enter coefficient of x^2")
a=utility_obj.get_int()
print("Enter coefficient of x")
b=utility_obj.get_int()
print("Enter contant c")
c=utility_obj.get_int()

first_root,second_root = utility_obj.get_quadratic_roots(a,b,c)

print("First Root =>"+str(first_root))
print("Second Root => "+str(second_root))