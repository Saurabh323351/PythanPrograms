import json
from com.bridgelabz.util.utility import Utility
d = {
    "name": "saurabh",
    "surname": "singh",
    "age": 22,
    "marks": [100, 200, 300],
    "Address": {
        "chawl": "Rajput chawl",
        "pincode": 400101,
        "Area": "Kandivali"
    }

}

# print(json.dumps(d,indent=4,separators=('.','=s'),sort_keys=True))# we can give indent also
"""
  we can give indent also 
 we can give separators also  
 we can sort by using sort_keys=True 
"""
#
# # print(json.dumps({"1":"saurabh",
# #                   "2":"singh"}))
# print(json.dumps("hello json"))
# print(json.dumps([10, 20, "saurabh"]))
# print(json.dumps((1, 2, 3, 4, 5)))
# print(json.dumps(100000))
# print(json.dumps(True))
# print(json.dumps(18.05))
# print(json.dumps(None))

# with open('demo.json','w') as jf:
#     jf.write(json.dumps(d,indent=2))

with open('demo.json', 'r') as jf:
    # print(type(jf.read())) # this read function gives  string value
    # that we should convert into dictionary sothat we can access our value
    # corresponding to each key

    json_string = jf.read()
    json_value = json.loads(json_string)
    # print(type(json_value))
    #
    # print(json_value["name"])

    # for i in json_value:
    #     print(i)

# name, weight, price
# per
# kg.
# Rice, Pulses and Wheats
#
d4 = {
    "Rice": [{
        "name": "Baasmati Rice",
        "weight":3,
        "price per kg": 5
    },
        {
            "name": "Brown Rice",
            "weight":2,
            "price per kg": 10
        }

    ],

    "Pulses": [{
        "name": "Moong Pulses",
        "weight": 5,
        "price per kg": 50
    }

    ],

    "Wheat": [{
        "name": "bajara",
        "weight": 12,
        "price per kg": 10
    }

    ]
}

with open('Inventory.json', 'w') as jf:
    jf.write(json.dumps(d4))

with open('Inventory.json', 'r') as jf:
    json_str = jf.read()
    json_value = json.loads(json_str)

    # print(type(json_value))

    # print(json_value["Rice"][0]["weight"] * json_value["Rice"][0]["price per kg"])


# total_amount_rice = json_value["weight"][0] * json_value["price per kg"][0]
# print(total_amount_rice)
#
# total_amount_pulses = json_value["weight"][1] * json_value["price per kg"][1]
# print(total_amount_pulses)
#
# total_amount_wheat = json_value["weight"][2] * json_value["price per kg"][2]
# print(total_amount_wheat)


class Inventory:

    def __init__(self, json_value, name=json_value["Rice"][0]["name"],weight=json_value["Rice"][0]["weight"],
                 price_per_kg=json_value["Rice"][0]["price per kg"]):
        self.category = {}
        self.existing_material = json_value
        # self.processExistingData()
        self.json_value = json_value
        self.name = name
        self.weight = weight
        self.price_per_kg = price_per_kg
        self.utility_obj=Utility()

    #
    # def processExistingData(self):
    #
    #     #Check if the existing material already exists
    #     if self.existing_material is not None:
    #
    #         # Set empty material details
    #         self.material_details = []
    #
    #         # Process the existing material to know how much material is being holding.
    #         for cat in self.existing_material:
    #
    #             # Set the category & Material type
    #             d = {
    #                 cat : ["Baasmati Rice", "Moong Pulses", "bajara"] # ( lambda self.existing_material[cat] )
    #             }
    #
    #             # Update category detail with the type of material
    #             self.category.update(d)
    #
    #             # Update this final dict to JSON. Update when new category or existing category is added or remove.
    #             self.d_final = {
    #                 cat: self.existing_material[cat]
    #             }
    #
    #             # Update this final dict to JSON. Update when new category or existing category is added or remove.
    #             # self.inventory_final.update(self.d_final)
    #
    #             # Material details list to search and add / remove
    #             self.material_details.append(self.existing_material[cat][0])
    #
    #     print('category ',self.category, self.material_details)
    #     print('details ',self.material_details)
    #
    # def processInventory(self, cat):
    #
    #     if self.inventory_final is None:
    #         for cat in self.existing_material:
    #             # Update this final dict to JSON. Update when new category or existing category is added or remove.
    #             self.d_final = {
    #                 cat: self.existing_material[cat]
    #             }
    #
    #             # Update this final dict to JSON. Update when new category or existing category is added or remove.
    #             self.inventory_final.update(self.d_final)
    #     else:
    #         # Check if the category exists in the d_final to make sure its added.
    #         if self.d_final[cat] is None: # Check condition
    #             # Update only new cateogry add
    #             self.d_final = {
    #                 cat: self.existing_material[cat]
    #             }
    #         # else:
    #             # update exisiting category with the material details
    #
    #
    #         # Update this final dict to JSON. Update when new category or existing category is added or remove.
    #         # self.inventory_final.update(self.d_final)
    #

    def inventory_materials(self):
        json_keys = self.json_value.keys()
        for key in json_keys:
            print(key)
    print('Enter choice u want')
    def see_category(self):
        index=0
        for i in self.json_value:

            if i == 'Rice':
                for j in json_value["Rice"]:
                    print(index,j)
                    index+=1
                choice=self.utility_obj.get_int()
                price_per_kg=json_value["Rice"][choice]["price per kg"]
                self.set_price_per_kg(price_per_kg)
                print('Enter how much you want to buy')
                weight=self.utility_obj.get_int()
                self.set_weight(weight)
                print('your total price is ')
                print(self.get_price())




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


i_obj = Inventory(json_value)
i_obj.set_name("Baasmati Rice1")
# print(i_obj.get_name())
# print(i_obj.get_weight())
# print(i_obj.get_weight_per_kg())
# print(i_obj.get_price())
# print(i_obj.a)

i_obj.inventory_materials()
i_obj.see_category()
#
# class Learning:
#
#     def __init__(self,a=0):
#         self.set_speed(a)
#
#     def get_speed(self):
#         return self._speed
#
#     def set_speed(self,a):
#
#         if a<40:
#             self._speed=a
#         else:
#             self._speed=None
#
#
# obj=Learning()
# obj.set_speed(30)
# print(obj.get_speed())
