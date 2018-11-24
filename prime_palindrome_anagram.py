from com.bridgelabz.util.utility import Utility

utility_obj=Utility()
store_prime_palindrome=utility_obj.get_palindrome_prime()

print("The Prime Numbers which are Palindrome are as follows")
for i in store_prime_palindrome:
    print(i)

print("The Preme Numbers which are Anagram are as follows")
utility_obj.get_anagram_prime()
