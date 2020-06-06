# Creating dictionaries
# Key:Value pairs separated by colon
new_dict = {}
new_dict['Dog'] = "woof"

squares = {2: 4, 3: 9, 4: 16, 5: 25}

ages = {
    'Bob': 40,
    'Mary': 45,
    'John': 35,
}


# Accessing dictionaries
print(ages['Bob'])
ages['John'] = 18
ages['John'] += 3
ages['Santa']           # KeyError
ages['Santa'] = None


# Miscellaneous
keys are unordered
keys must be immutable
if you want to change a key - you have to delete and add new key/value pair
values can be anything and be changed in place
you can only look up values by keys, can't look up keys by value
dictionaries do not have duplicate keys, if you add a key that is already there it will overwrite the old key/value pair


# Dictionary functions
ages.get('John')        # Returns 21 (because we updated his age)
ages.get('Apple')       # Returns None (instead of an error)
ages.get('Apple', 50)   # Returns 50 (set second paramater as default value)
ages.keys()             # Returns dict_keys(['Bob', 'Mary', 'John', 'Apple'])
list[ages.keys()]       # Converts to a list ['Bob', 'Mary', 'John', 'Apple']
ages.values()           # Returns dict_values([40, 45, 21, 50])
ages.items()            # Returns dict_items([('Bob', 40), ('Mary', 45), ('John', 35), ('Apple', 50)])
ages.pop('Apple')       # Removes the pair, returns the value
del ages['John']        # Removes the pair, but doesn't return anything
len(ages)               # Returns 3
ages.clear()            # Resets ages to {}
'John' in ages          # Returns True
40 in ages              # Returns False (does not check value in dict)


# Dictionary looping
for key in ages:
    print(key)
    print(ages[key])
    
for value in ages.values():
    print(value)

for (key, value) in ages.items():
    print(key, value)


# Reverse a dictionary: keys and values swap
ages = {
    'Mehran': 50,
    'Gary': 70,
    'Chris': 32,
}

reversed = {}
for (k, v) in ages.items():
    reversed[v] = k
print(reversed)
    
    
ages = {
    'Mehran': 50,
    'Gary': 70,
    'Chris': 32,
    'Brahm': 23,
    'Adele': 32,
    'Lionel': 32,
    'Rihanna': 32,
    'Stephen': 32,
    'Skrillex': 32
}

reversed = {}
for (k, v) in ages.items():
    if v in reversed:
        reversed[v].append(k)
    reversed[v] = [k]
print(reversed)


key -> Hash Fn -> array index
hash_int = hash(key);