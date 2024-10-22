import json
person = '{"name": "Umer", "Languages" : ["English","Urdu"]}'

 
person_dict = json.loads(person)
print(person_dict)
print(person_dict["Languages"])

# Python read JSON File
with open('person.json', 'r') as f:
    data = json.load(f)
    
print(data)

#Python Convert to JSON String

person1 = { 'name':'Umer','class':'python'}
person_json = json.dumps(person1)

print(person_json)


# Writing json TO THE file

std = {"name":"Zain", "Languages": ["English", "Urdu"],
       "Status": True, "age":20}

with open('std.json', 'w') as json_file:
    json.dump(std,json_file)