from com.bridgelabz.utility.Utility import Utility


utility_obj = Utility()
print("Enter Year")
Year = utility_obj.get_string()
utility_obj.isleap_year(Year)