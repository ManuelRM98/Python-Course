#Dictionary in Python
numbers = {1:"one", 2:"two", 3:"three"}

print(numbers)

#To look for something in the dictionary

print(numbers[2])

information = {"name": "Manuel", "last name": "Rodriguez", "height":"1.86", "age":"28"}

del information["age"]
print(information)

#methods of dictionaries

keys_dict = information.keys()
print(keys_dict)
print(type(keys_dict))

value_dict = information.values()
print(value_dict)

pairs = information.items()
print(pairs)

#You can create a dictionary of dictionaries

contacts = {"Manuel":{"last name": "Rodriguez", "height":"1.86", "age":"28"},
            "Mateo":{"last name": "Ramirez", "height":"1.75", "age":"22"}}

print(contacts["Manuel"])
print(contacts["Mateo"])