from com.bridgelabz.util.utility import Utility


utility_obj = Utility()
print("Enter Year")
Year = utility_obj.get_string()
print(utility_obj.isleap_year(Year))