from com.bridgelabz.util.utility import Utility


utility_obj=Utility()
print("Enter decimal number to convert into binary representation")
DECIMAL_VALUE=utility_obj.get_int()

BINARY_REPRESENTATION=Utility.to_binary(DECIMAL_VALUE)
print(str(DECIMAL_VALUE)+" -> binary representation -> "+str(BINARY_REPRESENTATION))
