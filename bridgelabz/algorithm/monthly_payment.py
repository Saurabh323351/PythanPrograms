from com.bridgelabz.util.utility import Utility


utility_obj = Utility()
print("Enter principle")
PRINCIPLE=utility_obj.get_int()
print("Enter Rate")
RATE=utility_obj.get_int()
print("Enter Year")
YEAR=utility_obj.get_int()
Utility.monthly_payment(PRINCIPLE,RATE,YEAR)