from com.bridgelabz.utility.Utility import Utility
import sys

utility_obj=Utility()
# x_coordinate = int(sys.argv[1])
# y_coordinate = int(sys.argv[2])
print("Enter x_coordinate ")
x_coordinate =utility_obj.get_int()
print(" Enter y_coordinate ")
y_coordinate =utility_obj.get_int()


euclidean_distance=utility_obj.get_euclidean_distance(x_coordinate,y_coordinate)
print(euclidean_distance)