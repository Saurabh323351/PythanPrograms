import json

from com.bridgelabz.util.object_oriented_util import Inventory


def inventory_runner():
    with open('../util/Inventory.json', 'r') as jf:
        json_str = jf.read()
        jf.close()
        json_value = json.loads(json_str)

    i_obj = Inventory(json_value)

    i_obj.inventory_materials()
    i_obj.see_category()


if __name__ == "__main__":
    inventory_runner()
