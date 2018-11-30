from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *

utility_obj=Utility()

logic_obj = Logic()

print('Enter Month')
month=utility_obj.get_int()
print('Enter Year')
year=utility_obj.get_int()
logic_obj.calender_stack(month,year)