import random
import sys
from array import array

class Utility:

    def __init__(self):
        pass

    def get_int(self):
        return int(input(""))

    def get_string(self):
        return input("")

    def replace_str(self, string, replace, user_string):

        return string.replace(replace, user_string)

    def get_probability(self, times):
        head = 0

        for i in range(0, times):
            r = random.randint(0, 1)
            if r == 1:
                head += 1

        tail = times-head

        head_percentage=((head/times)*100)
        tail_percentage=((tail / times) * 100)
        return head_percentage, tail_percentage

    def isleap_year(self, year):
        if len(year) < 4:
            print("enter year having 4 digit ")
            year = utility_obj.get_string()
            utility_obj.isleap_year(year)

        else:
            year = int(year)
            if year % 100 == 0 and year % 400 == 0:
                print(str(year) + " is a Leap year")

            else:
                print(str(year) + " is not a leap year")

    def power(self, limit):
        #store_value=[]
        #count=0
        if 0 > limit or limit >30:
            print("Enter value greater than equal to zero but less than 31")
            limit=utility_obj.get_int()
            utility_obj.power(limit)

        else:

            for i in range(0,limit+1):
                value = pow(2,i)
                print(value)

    def get_nth_harmonic_value(self,harmonic_value):
        sum=0
        for i in range(1,harmonic_value+1):
            sum += 1/i
        print(sum)

    def get_prime_factors(self):
        list = []
        count = 0
        print("Enter Number to find Prime Factors =>")
        num=utility_obj.get_int()
        Range = num
        is_prime = True
        for i in range(Range):
            if i == 0 or i == 1:
                continue
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:

                while num % i == 0:
                    # print(i)
                    list.insert(count, i)
                    count += 1
                    num = num / i

        return list


    def get_gambling_result(self,stake,goal,times):
        cash=stake
        win_count=0
        lose_count=0
        i=0
        while (cash!=0 or cash==goal) and i<times:
            random_number=random.randint(0, 1)
            i += 1
            if random_number==1:
                cash += 1
                win_count+=1

            elif random_number==0:
                cash-=1
                lose_count+=1

            if cash==goal:
                break

        win_percent = (win_count / (win_count + lose_count)) * 100
        lose_percent = (lose_count / (win_count + lose_count)) * 100
        return win_count,win_percent,lose_percent


    def coupan_generator(self,no_of_coupans):
        store_coupans=[]
        random_number_count=0
        while len(store_coupans)<= no_of_coupans:
            random_number=random.randint(1,50)
            random_number_count+=1

            if store_coupans.__contains__(random_number)==False:
                store_coupans.append(random_number)


        return random_number_count,store_coupans


    def get_2d__input(self,row,column):

        two_d_array = [[0 for j in range(column)] for i in range(row)]

        for i in range(0,row):
            for j in range(0,column):
                two_d_array[i][j]=Utility().get_int()

        return two_d_array

        #print(two_d_array)
utility_obj = Utility()
#utility_obj.get_2d__input(3,3)