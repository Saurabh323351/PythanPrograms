from com.bridgelabz.util.utility import Utility
utility_obj = Utility()
print("Enter Stake")
stake=utility_obj.get_int()
print("Enter goal")
goal=utility_obj.get_int()
print("Enter number of times you want to play")
no_of_times=utility_obj.get_int()


win_count,win_percent,lose_percent=utility_obj.get_gambling_result(stake,goal,no_of_times)
print(win_count)

print(win_percent)
print(lose_percent)