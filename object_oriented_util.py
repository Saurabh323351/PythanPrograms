import json

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
    pass
