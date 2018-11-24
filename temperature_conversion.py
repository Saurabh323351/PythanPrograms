from com.bridgelabz.util.utility import Utility


utility_obj = Utility()
print("1.convert Celsius to Fahrenheit ")
print("2.convert Fahrenheit to Celsius ")
CHOICE=utility_obj.get_int()
TEMPERATURE=Utility.temperature_conversion(CHOICE)
print(TEMPERATURE)