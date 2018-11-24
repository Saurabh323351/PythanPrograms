from com.bridgelabz.util.utility import Utility

utility_obj = Utility()
print("Enter Date ")
DATE = utility_obj.get_int()
print("Enter Month")
MONTH = utility_obj.get_int()
print("Enter Year")
YEAR = utility_obj.get_int()

Utility.day_of_week(DATE, MONTH, YEAR)
