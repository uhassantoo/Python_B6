#create a dict

country = {
    'Pakistan': 'Lahore',
    'England': 'Karachi',
    'UAE': 'Abu Dhabi',
    'ID' : 123
}

print('Countries Details:', country)

#immutable 
#keys must be immutable

#Access 
print('Country Capital:', country.get('ID'))
print('Country Capital:', country['Pakistan'])

# Add Item
country['Italy'] = 'Rome'

print(country)

#remove dictionary 
del country['England']
print(country)

#clear method
# country.clear()
# print(country)

#change item in dict

country['Italy'] = 'Istanbul'
print(country)

# dict with for loop print key
for coun in country:
    print(coun)
    
# dict wit for loop print value

for coun in country:
    captial =  country[coun]
    print(captial)

#len function in dict
print(len(country))

#keys dict

dictkey = country.keys()
print(dictkey)