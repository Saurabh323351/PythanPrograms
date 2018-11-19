from com.bridgelab.utility.Utility import Utility

utility_obj = Utility()
print("Enter Number of Rows")
row=utility_obj.get_int()
print("Enter Number of Columns")
column=utility_obj.get_int()


two_d_array=utility_obj.get_2d__input(row,column)


for i in range(0, row):
    for j in range(0, column):
        print(two_d_array[i][j], end=" ")

    print("")