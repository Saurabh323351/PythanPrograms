from com.bridgelabz.utility.Utility import Utility
utility_obj=Utility()

print("Enter Number")
N=utility_obj.get_int()
utility_obj.number_guess_game(0, N-1)