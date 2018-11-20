import random
import sys
from array import array
from math import sqrt,floor,ceil
import time
from timeit import default_timer

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
        store_value=[]
        #count=0
        if 0 > limit or limit >30:
            print("Enter value greater than equal to zero but less than 31")
            limit=utility_obj.get_int()
            if 0 > limit or limit > 30:
                return utility_obj.power(limit)

        if  0<=limit<=30:

            for i in range(0,limit+1):
                value = pow(2,i)
                store_value.append(value)
            return store_value

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
        return win_count, win_percent, lose_percent


    def coupan_generator(self, no_of_coupans):
            store_coupans = []
            random_number_count = 0
            while len(store_coupans) < no_of_coupans:
                random_number = random.randint(1, 50)
                random_number_count += 1

                if store_coupans.__contains__(random_number) == False:
                    store_coupans.append(random_number)

            return random_number_count, store_coupans


    def get_2d__input(self, row, column):

            two_d_array = [[0 for j in range(column)] for i in range(row)]

            for i in range(0, row):
                for j in range(0, column):
                    two_d_array[i][j] = Utility().get_int()

            return two_d_array

    def find_triplet(self, store_values):
            size = len(store_values)

            for i in range(0, size - 2):

                for j in range(i + 1, size - 1):

                    for k in range(j + 1, size):

                        if (store_values[i] + store_values[j] + store_values[k]) == 0:
                            print(store_values[i], end=" ")
                            print(store_values[j], end=" ")
                            print(store_values[k], end=" ")
                            print("")


    def get_euclidean_distance(self,x_coordinate,y_coordinate):

        x=x_coordinate
        y=y_coordinate

        euclidean_distance=sqrt(x**2+y**2)
        return euclidean_distance


    def get_elapsed_time(self,choice):

        if choice==1:
            print("StopWatch Started")
            start_time=default_timer()

        choice=Utility().get_int()
        if choice==2:
            stop_time=default_timer()

            elapsed_time_in_seconds=stop_time-start_time
            print(elapsed_time_in_seconds)


    def get_quadratic_roots(self,a,b,c):

        delta=(b*b-4*a*c)

        first_root=(-b+sqrt(delta))/2*a

        second_root=(-b-sqrt(delta))/2*a

        return first_root,second_root


    def get_effective_temperature(self,temperature,velocity):
        t=temperature
        v=velocity

        if t>=51 or (v<=2 or v>=121):
            print("Enter temperature value less than equal to 50 \n and velocity value greater than 2 but less than equal to 120")
            t=Utility().get_int()
            v = Utility().get_int()
            if t >= 51 or (v <= 2 or v >= 121):
              return  Utility().get_effective_temperature(t,v)


        if t<=50 and v<=120:
            windchill = 35.74 + 0.6215 * t + (.4275 * t - 35.75) * pow(v, 0.16)
            return windchill


    def anagram_detection(self,first_string,second_string):
        first_string=first_string
        s2=second_string
        first_string_list=[]
        s2_list=[]

        lower_string=first_string.lower()
        first_string=lower_string

        lower_string=''
        lower_string=s2.lower()
        s2=lower_string

        remove_space=''
        for i in range(0,len(first_string)):
            if first_string[i]==' ':
                continue

            remove_space+=first_string[i]

        first_string=remove_space

        remove_space = ''
        for i in range(0, len(s2)):
            if s2[i] == ' ':
                continue
            remove_space += s2[i]

        s2 = remove_space

        for i in first_string:
            first_string_list.append(i)


        for i in range(0,len(first_string_list)-1):

            for j in range(i+1,len(first_string_list)):
                temp=''
                if first_string_list[i]>first_string_list[j]:
                    temp=first_string_list[i]
                    first_string_list[i]=first_string_list[j]
                    first_string_list[j]=temp

        first_string=''
        for i in range(0, len(first_string_list)):
            first_string=first_string+first_string_list[i]



        for i in s2:
            s2_list.append(i)

        for i in range(0,len(s2_list)-1):

            for j in range(i + 1,len(s2_list)):
                temp = ''
                if s2_list[i] > s2_list[j]:
                    temp = s2_list[i]
                    s2_list[i] = s2_list[j]
                    s2_list[j] = temp

        s2 = ''
        for i in range(0, len(s2_list)):
            s2 = s2 + s2_list[i]

        s3=''
        if first_string==s2:
            print("Both Strings are Anagram of each other")


        else:
            print('Both Strings are not Anagram of each other')

    def get_prime(self):
        list = []
        is_prime = True
        for i in range(1001):
            if i == 0 or i == 1:
                continue
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                list.append(i)
        return list

utility_obj = Utility()
