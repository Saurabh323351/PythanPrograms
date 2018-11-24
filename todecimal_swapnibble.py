from com.bridgelabz.util.utility import Utility

utility_obj=Utility()
print("Enter decimal value")
decimal_value=utility_obj.get_int()
decimal_value=Utility.todecimal_of_swap_nibble(decimal_value)
print(decimal_value)
