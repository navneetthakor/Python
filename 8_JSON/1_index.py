"""
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.
"""

# Python has a built-in package called json, which can be used to work with JSON data.
import json

"""
Json to python
"""
myJsonText = """
{ "name" : "Navneetkumar R. Thakor",
"age" : 21
}
"""

result = json.loads(myJsonText)
print(type(result))
print(result)
print(result['name'])


"""
python dictionary to json
"""

my_dict = {
    "home_town" : "Anand",
    "work_town" : "Ahemdabad"
}
result = json.dumps(my_dict, indent=4) # provides indentation to make string readable
print("\n---")
print(type(my_dict))
print(type(result))
print(result)
