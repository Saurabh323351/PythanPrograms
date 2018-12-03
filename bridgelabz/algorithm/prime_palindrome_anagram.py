from com.bridgelabz.util.utility import Utility

utility_obj=Utility()
store_prime_palindrome=utility_obj.get_palindrome_prime()

print("The Prime Numbers which are Palindrome are as follows")
for i in store_prime_palindrome:
    print(i)

print("The Prime Numbers which are Anagram are as follows")
prime_anagram=[]
prime_anagram=utility_obj.get_anagram_prime()
for i in prime_anagram:
    print(i)
