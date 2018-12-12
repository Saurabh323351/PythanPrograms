import json
import re
import random

from com.bridgelabz.util.datastructure_util import Queue
from com.bridgelabz.util.utility import Utility
from wheel.signatures.djbec import P

from com.bridgelabz.util.utility import Utility


class ObjectOrientedPrograms:
    pass


class Inventory:
    with open('../util/Inventory.json', 'r') as jf:
        json_str = jf.read()
        jf.close()
        json_value = json.loads(json_str)

    def __init__(self, json_value, name=json_value["Rice"][0]["name"], weight=json_value["Rice"][0]["weight"],
                 price_per_kg=json_value["Rice"][0]["price per kg"]):

        self.existing_material = json_value

        self.json_value = json_value
        self.name = name
        self.weight = weight
        self.price_per_kg = price_per_kg
        self.utility_obj = Utility()

        # print("\033[1;32;40m Bright Green  \n")
        print("\n<--- Just Look at the Materials that We have in our Inventory and Select Accordingly --->\n")

    list_keys = []
    key_index = 0
    material_chosen = ''

    def inventory_materials(self):

        json_keys = self.json_value.keys()
        for key in json_keys:
            self.list_keys.append(key)
        for i in self.list_keys:
            print(self.key_index, i)
            self.key_index += 1

        self.key_index = self.utility_obj.get_int()
        self.material_chosen = self.list_keys[self.key_index]

    def see_category(self):
        index = 0

        for i in self.json_value:

            if i == self.material_chosen:
                print("Now Look at the Category for ->", self.material_chosen, "<- that We have in our Inventory\n")

                for j in self.json_value[self.material_chosen]:
                    print(index, j)
                    index += 1

                index_update = index
                print(index_update, "If you did not find your match in our listed Category of ", self.material_chosen,
                      '\n  Then Just add your required category of', self.material_chosen,
                      '\n  You can get it by Tomorrow\n')

                choice = self.utility_obj.get_int()
                if index_update == choice:
                    self.update_category()
                    return
                else:
                    price_per_kg = self.json_value[self.material_chosen][choice]["price per kg"]
                    self.set_price_per_kg(price_per_kg)
                    print('Enter how many kilograms you want to buy')
                    weight = self.utility_obj.get_int()
                    self.set_weight(weight)
                    print('your total price is ')
                    print(self.get_price())

    def update_category(self):
        print("Enter Your Requirement Now\n")
        user_requirement = self.utility_obj.get_string()
        with open('../util/Inventory.json', 'r') as jf:
            json_str = jf.read()
            jf.close()
            json_value = json.loads(json_str)
        with open('../util/Inventory.json', 'w') as jf:
            json_value[self.material_chosen].append({"name": user_requirement,
                                                     "weight": 1,
                                                     "price per kg": 50

                                                     })

            jf.write(json.dumps(json_value))
            jf.close()

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_price_per_kg(self):
        return self.price_per_kg

    def set_price_per_kg(self, price_per_kg):
        self.price_per_kg = price_per_kg

    def get_price(self):
        price = self.get_price_per_kg() * self.get_weight()
        return price


class RegularExpression:

    def __init__(self):
        pass

    def regex(self):
        string = ' Hello <<name>>, We have your full name as <<full name>> in our system.\n your contact number is 91-xxxxxxxxxx.\n Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016. '
        template = ['<<name>>', '<<full name>>', 'xxxxxxxxxx', '01/01/2016']
        list = ['Enter Your First Name', 'Enter Your Full Name', 'Enter Your Mobile Number', "Enter Today's Date"]

        for i in range(4):
            print(' =>', list[i])
            replaced_string = re.sub(template[i], Utility().get_string(), string, 1)
            string = replaced_string

        return string


with open('../util/Stock Report', 'r') as jf:
    json_str = jf.read()
    jf.close()
    json_value = json.loads(json_str)

    # print(json_value)


class StockReport:

    def __init__(self, json_value):
        self.json_value = json_value

    def stock_report(self):
        count = 0
        count1 = 1
        for i in range(len(json_value['Stock Report'])):
            count1 = 1
            for key in (json_value['Stock Report'][i]):

                if i == 0 and count == 0:
                    for key1 in (json_value['Stock Report'][0]):
                        print(key1, end='  ')
                        count += 1
                        if count == len(json_value['Stock Report'][0]):
                            print(' Total Price ', end='')

                    print()

                print(json_value['Stock Report'][i][key], end='             ')
                if count1 == len(json_value['Stock Report'][i]):
                    print(
                        json_value['Stock Report'][i]['Number of Share'] * json_value['Stock Report'][i]['Share Price'],
                        end='  ')
                count1 += 1
            print()


sr = StockReport(json_value)


class DeckOfCards:

    def __init__(self):
        pass

    def shuffle(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        list_cards = []
        card_suits = ''

        while len(list_cards) < 36:
            for i in range(0, 9):

                cards_rank = ''

                random_no = random.randint(1, 13)

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)
                cards_rank = cards_rank + ' ' + suits[random_no_suits]

                if list_cards.__contains__(cards_rank) is False:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0
        for i in range(row):

            for j in range(column):
                two_d_array[i][j] = list_cards[index]
                index += 1

        return list_cards, two_d_array


card = DeckOfCards()


class Player:

    def __init__(self, list_cards, utility_obj, queue):
        self.list_cards = list_cards
        self.utility_obj = utility_obj
        self.queue = queue

    def replacing(self):
        i = 0
        while i < len(self.list_cards):

            if bool(re.search('Ace', self.list_cards[i])):
                self.list_cards[i] = re.sub('Ace', '14', self.list_cards[i], 1)

            if bool(re.search('Jack', self.list_cards[i])):
                self.list_cards[i] = re.sub('Jack', '11', self.list_cards[i], 1)

            if bool(re.search('Queen', self.list_cards[i])):
                self.list_cards[i] = re.sub('Queen', '12', self.list_cards[i], 1)

            if bool(re.search('King', self.list_cards[i])):
                self.list_cards[i] = re.sub('King', '13', self.list_cards[i], 1)

            i += 1

        ranks = []
        number = []
        i = 0
        while i < len(self.list_cards):
            ranks.append(self.list_cards[i].split(" "))

            number.append(int(ranks[i][0]))
            i += 1

        number = Utility().bubblesort_for_integer(number)
        i = 0
        sorted_card = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        while i < 36:

            string = ''
            random_no = random.randint(0, 3)
            string = suits[random_no]
            string = str(number[i]) + " " + string

            while sorted_card.__contains__(string) is True:
                random_no = random.randint(0, 3)
                string = suits[random_no]
                string = str(number[i]) + ' ' + string

            if sorted_card.__contains__(string) is False:
                sorted_card.append(string)

            i += 1

            i = 0
            while i < len(sorted_card):

                if bool(re.search('14', sorted_card[i])):
                    sorted_card[i] = re.sub('14', 'Ace', sorted_card[i], 1)

                if bool(re.search('11', sorted_card[i])):
                    sorted_card[i] = re.sub('11', 'Jack', sorted_card[i], 1)

                if bool(re.search('12', sorted_card[i])):
                    sorted_card[i] = re.sub('12', 'Queen', sorted_card[i], 1)

                if bool(re.search('13', sorted_card[i])):
                    sorted_card[i] = re.sub('13', 'King', sorted_card[i], 1)

                i += 1

        player_objs = []
        limit = 0
        index = 9
        for i in range(0, 4):
            player_objs.append(Player(card.shuffle(), Utility(), Queue()))

            for sorted_cards in sorted_card:
                if limit < index:
                    player_objs[i].queue.enqueue(sorted_card[limit])

                    limit += 1
            index += 9

        for i in range(0, 4):
            print('Player', i + 1, '\n', '----------')
            print(player_objs[i].queue.show())
            print('\n')


class StockAccount:
    pass


#
# P = {
#     "Person": [{
#         "Name": "Saurabh",
#         "Email id": "singh.saurabh3333@gmail.com",
#         "Address": "Kandivali",
#         "Contact": 9137722561,
#         "Total Balance": 10000
#     },
#         {
#             "Name": "Aman",
#             "Email id": "singh.aman33@gmail.com",
#             "Address": "Kandivali",
#             "Contact": 9137722558,
#             "Total Balance": 10000
#         }
#     ]
#
# }
#
# with open('../util/Person.json', 'w') as person_jf:
#     person_jf.write(json.dumps(P))
#     person_jf.close()

class Person:

    def __init__(self, stock_jf, utility_obj, person_json_value):
        self.stock_jf = stock_jf
        self.utility_obj = utility_obj
        self.person_json_value = person_json_value
        self.method_controller()

    def method_controller(self):
        print('---->''WELCOME TO SHARE MARKET', '<----')
        print("  1.Existing Customer\n  2.New Customer\n  3.Add New Company")
        ch = self.utility_obj.get_int()

        if ch == 1:

            i = 0
            print('Enter Your Name')
            existing_person = self.utility_obj.get_string()
            while i < len(person_json_value["Person"]):
                if person_json_value["Person"][i].get('Name', -1) == existing_person:
                    index = i

                i += 1
            print('Do You Want Your Details? Y / N')
            detail_choice = self.utility_obj.get_string()
            if detail_choice == 'Y' or detail_choice == 'y':
                print(person_json_value["Person"][index])
            if detail_choice == 'N' or detail_choice == 'n':
                pass

            print('1.Buy Share \n 2.Sale Share')
            choice = self.utility_obj.get_int()
            if choice == 1:
                self.buy_share(index)

            if choice == 2:
                self.sell_share(index)

        if ch == 2:
            print("You Need to Register Yourself first.So We request you to Kindly provide your details accordingly")
            self.add_new_person()

            print('Enter Your Name to see available option for you')
            existing_person = self.utility_obj.get_string()
            i = 0
            while i < len(person_json_value["Person"]):
                if person_json_value["Person"][i].get('Name', -1) == existing_person:
                    index = i

                i += 1
            print('Do You Want Your Details? Y / N')
            detail_choice = self.utility_obj.get_string()
            if detail_choice == 'Y' or detail_choice == 'y':
                print(person_json_value["Person"][index])
            if detail_choice == 'N' or detail_choice == 'n':
                pass

            print('1.Buy Share \n 2.Sale Share')
            choice = self.utility_obj.get_int()
            if choice == 1:
                self.buy_share(index)
                exit()
            if choice == 2:
                self.sell_share(index)
                exit()
        if ch == 3:
            self.add_new_company()
            print('Your Company Details Added Successfully')
            exit()

    def add_new_person(self):
        print('Enter Your Name')
        name = self.utility_obj.get_string()
        print('Enter Your Email Id')
        emailid = self.utility_obj.get_string()
        print('Enter Your Address')
        address = self.utility_obj.get_string()
        print('Enter Your Contact Number')
        number = self.utility_obj.get_int()
        print("Enter Number of share if yoy have any ,else enter zero")
        share_no = balance = Utility().get_int()
        print('Enter Your Total Balance')
        balance = Utility().get_int()

        new_person_dict = {"Name": name,
                           "Email id": emailid,
                           "Address": address,
                           "Contact": number,
                           "Number of Share": share_no,
                           "Total Balance": balance}

        with open('../util/Person.json', 'w') as person_jf:
            person_json_value['Person'].append(new_person_dict)

            person_jf.write(json.dumps(person_json_value))
            person_jf.close()

    def add_new_company(self):
        print('Enter Stock Name or company Name')
        name = self.utility_obj.get_string()
        print('Enter Your Number of share')
        number = self.utility_obj.get_int()
        print('Enter Your Price per share')
        price = Utility().get_int()

        new_stock_dict = {"Stock Name": name,

                          "Number of Share": number,

                          "Share Price": price}

        with open('../util/Stock Report.json', 'w') as stock_jf:
            self.stock_jf['Stock Report'].append(new_stock_dict)

            stock_jf.write(json.dumps(self.stock_jf))
            stock_jf.close()

    def buy_share(self, index):
        for i in range(len(self.stock_jf['Stock Report'])):
            print(i, self.stock_jf['Stock Report'][i])

        print('Enter Which Company Share you want to buy')
        choice = self.utility_obj.get_int()

        print('Enter Number of Share You want to buy')
        buy_share = self.utility_obj.get_int()
        each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
        amount_pay = buy_share * each_share_price
        print(' --> `', amount_pay, '<--will be deducted from your total balance')

        person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
        print('Now Your Updated Balance is ', person_updated_balance)
        person_updated_share = person_json_value['Person'][index]['Number of Share'] + buy_share
        print('Now Your Updated Number of share is ', person_updated_share)

        with open("Person.json", "w") as jf:
            person_json_value['Person'][index]['Total Balance'] = person_updated_balance
            person_json_value['Person'][index]['Number of Share'] = person_updated_share
            jf.write(json.dumps(person_json_value))
            jf.close()

        updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share

        with open("Stock Report", "w") as jf:
            self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
            jf.write(json.dumps(self.stock_jf))
            jf.close()

    def sell_share(self, index):
        print('Enter choice to sell your share to particular company')
        for i in range(len(self.stock_jf['Stock Report'])):
            print(i, self.stock_jf['Stock Report'][i])

        choice = self.utility_obj.get_int()

        print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
              'company')
        sell_share = self.utility_obj.get_int()
        updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share

        with open("Stock Report", "w") as jf:
            self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
            jf.write(json.dumps(self.stock_jf))
            jf.close()

        updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share
        print("Enter price for per share you want from company")
        person_share_price = self.utility_obj.get_int()
        person_updated_balance = self.person_json_value['Person'][index][
                                     "Total Balance"] + person_share_price * sell_share
        print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
        print('Now Your Updated Balance is ', person_updated_balance)
        print('Now Your Updated Number of share is ', updated_person_share)

        with open("Person.json", "w") as jf:
            person_json_value['Person'][index]['Total Balance'] = person_updated_balance
            person_json_value['Person'][index]['Number of Share'] = updated_person_share
            jf.write(json.dumps(person_json_value))
            jf.close()


with open('../util/Stock Report', 'r') as jf:
    json_str = jf.read()
    jf.close()
    json_value = json.loads(json_str)

with open('../util/Person.json', 'r') as person_jf:
    json_person_str = person_jf.read()
    person_jf.close()
    person_json_value = json.loads(json_person_str)

# person_obj = Person(json_value, Utility(), person_json_value)
# It manages Doctors by Name, Id, Specialization and Availability (AM,  PM or both).
# It manages Patients by Name, ID, Mobile Number and Age.

Doctors_dict = {
    "Doctors": [{
        "Name": "Saurabh Singh",
        "Id": 1,
        "Specialization": "Neurologist",

        " Availability": "PM"

    },
        {
            "Name": "Rajat Singh",
            "Id": 2,
            " Mobile Number": "Dermatologist",

            " Availability": "AM"

        }
    ]

}

Patients_dict = {
    "Patients": [{
        "Name": "Rohini Zade",
        "Id": 1,
        "Mobile Number": 9967493198,

        " Age": 23

    },
        {
            "Name": "Reshma Kale",
            "Id": 2,
            "Mobile Number": 9967493197,

            " Age": 22
        }
    ]

}

with open('../util/Person.json', 'w') as person_jf:
    person_jf.write(json.dumps(P))
    person_jf.close()


class Clinique:

    def __init__(self, utility_obj):
        self.utility_obj = utility_obj


clinique = Clinique(Utility())
