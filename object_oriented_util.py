import json

d = {
    "name": "saurabh",
    "surname": "singh",
    "age": 22,
    "marks":[100,200,300],
    "Address":{
        "chawl":"Rajput chawl",
        "pincode":400101,
        "Area": "Kandivali"
    }
    
}

# print(json.dumps(d,indent=4,separators=('.','=s'),sort_keys=True))# we can give indent also
"""
  we can give indent also 
 we can give separators also  
 we can sort by using sort_keys=True 
"""


# print(json.dumps({"1":"saurabh",
#                   "2":"singh"}))
print(json.dumps("hello json"))
print(json.dumps([10,20,"saurabh"]))
print(json.dumps((1,2,3,4,5)))
print(json.dumps(100000))
print(json.dumps(True))
print(json.dumps(18.05))
print(json.dumps(None))

# with open('demo.json','w') as jf:
#     jf.write(json.dumps(d,indent=2))

with open('demo.json','r') as jf:
    # print(type(jf.read())) # this read function gives  string value
                            #that we should convert into dictionary sothat we can access our value
                        #corresponding to each key

    json_string=jf.read()
    json_value=json.loads(json_string)
    print(type(json_value))


    print(json_value["name"])

    for i in json_value:
        print(json_value.get(i,-1))