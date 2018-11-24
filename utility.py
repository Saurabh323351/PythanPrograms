import random
import sys
from array import array
from math import sqrt,floor,ceil
import time
from timeit import default_timer
import cmath
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

            file_object=open("Matrix.txt","w")
            file_object.write(str(two_d_array))
            file_object.close()
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
        #z=complex(first_root,second_root)

        #x=complex((-b+sqrt(delta))/2*a,(-b-sqrt(delta))/2*a)
        return first_root,second_root
        #return x.real,0


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


        first_string_list=[]
        second_string_list=[]

        lower_string=first_string.lower()
        first_string=lower_string

        lower_string=''
        lower_string=second_string.lower()
        second_string=lower_string

        remove_space=''
        for i in range(0,len(first_string)):
            if first_string[i]==' ':
                continue

            remove_space+=first_string[i]

        first_string=remove_space

        remove_space = ''
        for i in range(0, len(second_string)):
            if second_string[i] == ' ':
                continue
            remove_space += second_string[i]

        second_string = remove_space

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



        for i in second_string:
           second_string_list.append(i)

        for i in range(0,len(second_string_list)-1):

            for j in range(i + 1,len(second_string_list)):
                temp = ''
                if second_string_list[i] >second_string_list[j]:
                    temp =second_string_list[i]
                    second_string_list[i] =second_string_list[j]
                    second_string_list[j] = temp

        second_string = ''



        for i in range(0, len(second_string_list)):
            second_string = second_string +second_string_list[i]

        s3=''
        if first_string==second_string:
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

    def get_palindrome_prime(self):
        store_prime = Utility().get_prime()

        s = ''
        store_palindrome_prime = []
        for i in store_prime:
            string = ''
            string = str(i)
            string1 = string
            count = -1
            reverse_string1 = ''

            for j in range(0, len(string1)):
                reverse_string1 += string1[count]
                count = count - 1

            string1 = ''
            if reverse_string1 == string:
                store_palindrome_prime.append(string)

        return store_palindrome_prime

    def get_anagram_prime(self):
        store_prime = Utility().get_prime()

        first_string_list = []
        second_string_list = []
        count = 0
        for each_index in range(0, len(store_prime) - 1):
            first_string_list = []
            s1 = str(store_prime[each_index])
            first_string = s1
            count = 0
            for i in first_string:
                first_string_list.append(i)

            for i in range(0, len(first_string_list) - 1):

                for j in range(i + 1, len(first_string_list)):
                    temp = ''
                    if first_string_list[i] > first_string_list[j]:
                        temp = first_string_list[i]
                        first_string_list[i] = first_string_list[j]
                        first_string_list[j] = temp

            first_string = ''
            for i in range(0, len(first_string_list)):
                first_string = first_string + first_string_list[i]

            for next_index in range(each_index + 1, len(store_prime)):

                second_string = str(store_prime[next_index])

                for i in second_string:
                    second_string_list.append(i)

                for i in range(0, len(second_string_list) - 1):

                    for j in range(i + 1, len(second_string_list)):
                        temp = ''
                        if second_string_list[i] > second_string_list[j]:
                            temp = second_string_list[i]
                            second_string_list[i] = second_string_list[j]
                            second_string_list[j] = temp

                second_string = ''
                for i in range(0, len(second_string_list)):
                    second_string = second_string + second_string_list[i]

                if first_string == second_string:
                    print(store_prime[next_index])
                    count += 1

                second_string_list = []

            if count >= 1:
                print(store_prime[each_index])

    @staticmethod
    def binary_search_for_int(store_user_value, search_item):

        store_user_value=Utility.insertionsort_for_integer(store_user_value)

        lower_limit=0
        upper_limit=len(store_user_value)-1

        while lower_limit<=upper_limit:

            mid_index=(lower_limit+upper_limit)//2

            if store_user_value[mid_index]==search_item:
                return mid_index

            if store_user_value[mid_index]>search_item:
                upper_limit=mid_index-1

            if store_user_value[mid_index]<search_item:
                lower_limit=mid_index+1

        print("Element Not Found")
        return -1

    @staticmethod
    def binary_search_for_string(store_user_value,search_item):

        store_user_value=Utility.insertionsort_for_string(store_user_value)
        #print(store_user_value)

        lower_limit = 0
        upper_limit = len(store_user_value) - 1

        while lower_limit<=upper_limit:

            mid_index=(lower_limit+upper_limit)//2

            if store_user_value[mid_index]==search_item:

                return mid_index


            if store_user_value[mid_index]<search_item:
                lower_limit=mid_index+1

            if store_user_value[mid_index]>search_item:
                upper_limit=mid_index-1

        print("Element Not Found")
        return -1



    @staticmethod
    def insertionsort_for_integer(number_list):

        for i in range(1,len(number_list)):
            index=i
            j=i-1
            while j>=0:

                if number_list[j]>number_list[index]:
                    temp=number_list[j]
                    number_list[j]=number_list[index]
                    number_list[index]=temp
                    index=j
                j=j-1

        return number_list

    @staticmethod
    def insertionsort_for_string(string_list):

       # string_list=['java','php','python','atom','javascript']

        for i in range(1,len(string_list)):

            index=i
            j=i-1
            while j>=0:

                if string_list[j]>string_list[index]:
                    temp=string_list[j]
                    string_list[j]=string_list[index]
                    string_list[index]=temp
                    index=j

                j=j-1

        return string_list


    @staticmethod
    def bubblesort_for_integer(integer_list):

        #integer_list=[50,60,1,2,80,0]

        for i in range(0,len(integer_list)-1):

            for j in range(i+1,len(integer_list)):

                if integer_list[i]>integer_list[j]:
                    temp=integer_list[i]
                    integer_list[i]=integer_list[j]
                    integer_list[j]=temp

        return integer_list

    @staticmethod
    def bubblesort_for_string(string_list):

        #string_list = ['java', 'aim', 'php', 'python', 'palindrome', 'bat']

        for i in range(0, len(string_list) - 1):

            for j in range(i + 1, len(string_list)):

                if string_list[i] > string_list[j]:
                    temp = string_list[i]
                    string_list[i] = string_list[j]
                    string_list[j] = temp

        return string_list

    def number_guess_game(self, lowerlimit, upperlimit):

        while lowerlimit <= upperlimit:
            if lowerlimit == upperlimit:
                print('Your Number is => ' + str(lowerlimit))
                print("Intermediary numbers is " + str(lowerlimit - 1) + " and " + str(lowerlimit + 1))
                return

            mid_value = (lowerlimit + upperlimit) // 2
            print('1. ' + str(lowerlimit) + ' - ' + str(mid_value))
            print('2. ' + str(mid_value + 1) + ' - ' + str(upperlimit))
            choice = Utility().get_int()
            if choice == 1:
                upperlimit = mid_value

            if choice == 2:
                lowerlimit = mid_value + 1


    @staticmethod
    def binarysearch_wordlist():
        file_obj = open("/home/bridgeit/PycharmProjects/BridgelabzProject/com/bridgelabz/util/WordList.txt", "r+")
        lines=['saurabh\n','rajat\n','suraj\n','aman\n']

        file_obj.writelines(lines)
        file_obj.close()

        file_obj=open("/home/bridgeit/PycharmProjects/BridgelabzProject/com/bridgelabz/util/WordList.txt","r")

        list=file_obj.readlines()
        file_obj.close()

        list=Utility.insertionsort_for_string(list)


        for i in range(0,len(list)):
            list[i]=list[i].strip() #here i am using strip() to remove \n from each element from list

        return list


    @staticmethod
    def insertionsort_file():
        file_obj=open("/home/bridgeit/PycharmProjects/BridgelabzProject/com/bridgelabz/util/WordList.txt","r")
        list=file_obj.readlines()

        for i in range(0, len(list)):
            list[i]=list[i].strip()


        list=Utility.insertionsort_for_string(list)
        return list


    @staticmethod
    def bubblesort_file():
        file_obj1= open("/home/bridgeit/PycharmProjects/BridgelabzProject/com/bridgelabz/util/NumberFile", "r+")
        list_number=[50,60,40,10,2,3,0]

        for i in list_number:
            file_obj1.write('%d\n' % i) #it is outdated method to write integer into file
            #file_obj1.write('{}'.format(i)) # this is modern method for writing integer into file

        #file_obj1.writelines(str(list_number))
        file_obj1.close()

        file_obj1=open("/home/bridgeit/PycharmProjects/BridgelabzProject/com/bridgelabz/util/NumberFile", "r")
        list_number=file_obj1.readlines()


        for i in range(0,len(list_number)):
            list_number[i]=list_number[i].strip()


        for i in range(0,len(list_number)):
            list_number[i]=int(list_number[i])

        list_number=Utility.bubblesort_for_integer()
        return list_number


    @staticmethod
    def get_vending_machine_result(num):


        i=-1
        notes_list=[1,2,5,10,50,100,500,1000]
        total_no_ofnotes=0
        vending_result={}



        while i>=-8:
            if  num//notes_list[i]>0 and num>0:
                num1=num//notes_list[i]
                num=num%notes_list[i]
                vending_result[str(notes_list[i])]=num1
                total_no_ofnotes+=num1
            i=i-1

        vending_result["Total Number of Notes"]=total_no_ofnotes
        return vending_result


    @staticmethod
    def day_of_week(date,month,year):

        d = date

        m = month
        y = year
        y0 = y-(14-m)//12
        x = y0+y0//4-y0//100+y0//400
        m0 =m+12*((14-m)//12)-2
        d0= (d + x + 31*m0 // 12)%7

        if d0==0:
            print("Sunday")
        if d0 == 1:
            print("Monday")
        if d0 == 2:
            print("Tuesday")
        if d0 == 3:
            print("Wednesday")
        if d0 == 4:
            print("Thursday")
        if d0 == 5:
            print("Friday")
        if d0 == 6:
            print("Saturday")


    @staticmethod
    def temperature_conversion(choice):

        if choice==1:
            print("Enter temperature in Celsius to convert in Fahrenheit ")
            c = Utility().get_int()
            f = (c * 9 // 5) + 32
            return f

        if choice == 2:
            print("Enter temperature in Fahrenheit  to convert in Celsius ")
            f = Utility().get_int()
            c=(f-32)*5//9
            return c



    @staticmethod
    def monthly_payment(principle,rate,year):

        P=principle
        R=rate
        Y=year
        n=12*Y
        r=R/12*100

        payment=(P*r)/1-pow((1+r),(-1*n))
        print(payment)


    @staticmethod
    def to_binary(decimal_value):

        binary_value=[]

        s=''
        while decimal_value>=1:
            binary_value.append(decimal_value%2)
            decimal_value=decimal_value//2

        for i in range(1,len(binary_value)+1):
            s=s+str(binary_value[-1*i])

        leftpadding_zeros=s.zfill(4)
        return leftpadding_zeros

    @staticmethod
    def todecimal_of_swap_nibble(decimal_value):


        binary_value=Utility().to_binary(decimal_value)
        left_padding=binary_value.zfill(8)
        binary_value=left_padding
        string1=''
        string1=string1+str(binary_value)
        string2=''
        string2=string2+string1[4:]
        string2=string2+string1[0:4]


        sum=0
        power=0
        for i in range(1,len(string2)+1):
            each_value=int(string2[-1*i])

            sum=sum+each_value*pow(2,power)
            power+=1
        decimal_value=sum
        return decimal_value


    @staticmethod
    def newtons_sqrt_method(number):
        c=number
        t=c

        while abs(t - c/t)>(1e-15)*t:
            t=(t + c/t)/2
        return t





utility_obj = Utility()


