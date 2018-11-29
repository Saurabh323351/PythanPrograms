from com.bridgelabz.util.datastructure_util import *
from com.bridgelabz.util.utility import *

utility_obj=Utility()
def cash_counter():

    bank_cash=1000
    print('Enter Number of People in the Queue')
    no_of_people=utility_obj.get_int()
    for i in range(0,no_of_people):
        queue.enqueue(i)


    print('Welcome To Bridgelabz Bank')
    for i in range(0,queue.size()):
        print('1.Deposit cash \n 2.Withdraw cash')
        choice=Utility().get_int()

        if choice==1:

            print("Enter Deposit Amount ")
            deposit_amount=Utility().get_int()
            bank_cash=bank_cash+deposit_amount
            queue.dequeue()

        if choice==2:
            print("Enter How much cash you want to Withdraw")
            withdraw_amount=utility_obj.get_int()

            if withdraw_amount<bank_cash:
                bank_cash=bank_cash-withdraw_amount
                queue.dequeue()

            if withdraw_amount>bank_cash:
                print('Insufficient Fund in Bank')
                print('1. Kindly enter cash within ' +str(bank_cash)+ ' range  \n 2.If you do not want and leave')
                withdraw_choice=utility_obj.get_int()

                if withdraw_choice==1:
                    print('Enter Withdraw Amount')
                    withdraw_amount=utility_obj.get_int()
                    if withdraw_amount<=bank_cash:
                        bank_cash=bank_cash-withdraw_amount
                    queue.dequeue()

                if withdraw_choice==2:
                    queue.dequeue()

        if i<queue.size():
            print('Next Person')

    print('Bank Balance => '+ str(bank_cash))

cash_counter()