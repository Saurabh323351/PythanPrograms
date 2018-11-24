from com.bridgelabz.util.utility import Utility

utility_obj=Utility()
print("Enter Number to get its squareroot ")
NUMBER=utility_obj.get_int()
SQUARE_ROOT=Utility.newtons_sqrt_method(NUMBER)
print("Square Root of Your Number  "+str(NUMBER)+ " is " + str(SQUARE_ROOT))
