'''
person = {"name":"Pranay","age" :"31"}  # intializing the dictionary
print(person["name"])                   # access using key 
person["age"] = "32"                    # update the exiting value
person["city"] = "Bangalore"            # add new key value pair
print(person)

'''

'''
# adding multiple keys and values in dictionary dynamically 

n = int(input("Enter the number : ")) # add the number of key value pairs you want to add in dictionary
person = {}
for i in range(n):
    key = input("Enter the key : ")     # enter the key and value dynamically
    value = input("Enter the value : ")
    person[key] = value

print(person)  

'''

'''
# Iterate Keys, Values & Items

person = {"name":"Pranay","age" :"31"}

for i in person.keys():  # iterate through keys
    print(i)

for i in person.values():  # iterate through values
    print(i)

for i, j in person.items():  # iterate through items
    print(i, j) 

'''


person = {"name": "Ravi", "age": 30}
print(person.get("name")) # key exists
print(person.get("city")) # missing -> None,no crash
print(person.get("city", "Not found")) # missing ->custom default
# person["city"] would raise KeyError instead
print("city" in person)







