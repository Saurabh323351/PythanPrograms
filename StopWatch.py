from com.bridgelabz.utility.Utility import Utility

utility_obj=Utility()

print("Use StopWatch => 1:Start\n" + "                 2:Stop")
choice=utility_obj.get_int()
utility_obj.get_elapsed_time(choice)