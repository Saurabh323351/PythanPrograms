from com.bridgelabz.util.utility import Utility

utility_obj = Utility()
print("Enter Temperature value")
temperature=utility_obj.get_int()
print("Enter Velocity value")
velocity=utility_obj.get_int()

windchill=utility_obj.get_effective_temperature(temperature,velocity)
print(windchill)
