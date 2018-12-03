from com.bridgelabz.util.utility import Utility
utility_obj=Utility()
print("Enter First string")
first_string=utility_obj.get_string()

print("Enter Second string")
second_string=utility_obj.get_string()
utility_obj.anagram_detection(first_string,second_string)