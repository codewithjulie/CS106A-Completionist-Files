# What are the characteristics of a dictionary?
mutable
keys must be immutable.  string, 
values can be either
can be reversed
can only look up values by keys, not the other way around
unordered


lst = ['a', 'b', 'c']
lst[0] == 'a'
'Apple' != 'apple'



# Creating a dictionary
dictionary = {}
for key in dictionary:
    dictionary[key] = values


people = {
    'Bob': 40,
    'Mary': 35,
    'John': 30
}

class List

def method()
    this will change your object

object.method() # Updates your object

function(object) # Returns new object, does not modify your object

# Accessing a dictionary:
people['Bob']                   # 40
people['Santa']                 # KeyError
people['John'] = 21             # Does not return, but updates 'John' value
people['John']                  # 21
people['John'] += 3             # Does not return, but updates 'John' value
people[30]                      # KeyError
people.get('John')              # 24
people.get('John', 0)           # 24
people.get('Santa', 0)          # 0, does not add Santa to dictionary
people.setdefault('Santa', 0)   # Adds Santa to dictionary with default 0
people.sort()                   # AttributeError
sorted(people)                  # ['Bob', 'John', 'Mary']
sorted(people, reverse=True)    # ['Mary', 'John', 'Bob']
sorted(people.values())         # [0, 30, 35, 40]
len(people)                     # 4
people.pop()                    # TypeError
people.pop('Santa')             # pops off Santa from people =(

people.clear()                  # now an empty dictionary, same as people = {}
del people                      # deleted the dictionary, dictionary no longer exists


# How can I print key value pairs in people?
for key, value in people.items():
    print(key, value)


# How can you get all keys or all values?

people_list = list(people.keys())
ages_list = list(people.values())


# Reverse dictionary?
people = {
    'Bob': 40,
    'Mary': 35,
    'John': 30,
    'Crystal': 30
}


people_reversed = {
    40: ['Bob'],
    35: ['Mary'],
    30: ['John']
}

'''
dictionaries are unordered

1. create - new empty dictionary
2. loop over the dictionary for keys
3. check if old key is in new dictionary
    old key == value
4. old value == key
5. 

'''

reversed_dictionary = {}
for key in people:
    old_value = people[key]
    reversed_dictionary.setdefault(old_value, [])
    # if old_value not in reversed_dictionary:
    #     reversed_dictionary[old_value] = []
    reversed_dictionary[old_value].append(key)


# Dictionaries in a dictionary
people = {'John': {'first': 'John', 'last': 'Doe', 'age': '27', 'sex': 'Male'},
          'Mary': {'first': 'Mary', 'last': 'Smith', 'age': '22', 'sex': 'Female'}}


# How would you access the 27?
people["John"]['age']

for person in people:
    if '33' in people[person].values():
        print("You found me")
    else:
        print("Not here")


# How would you print all the values for first?

for person in people:
    print(people[person]['first'])


# How would you get the keys for everyone who is male?

for person in people:
    if people[person]['sex'] == 'Male':
        print(person)


people = {'John': {'first': 'John', 'last': 'Doe', 'age': '27', 'sex': 'Male'},
          'Mary': {'first': 'Mary', 'last': 'Smith', 'age': '22', 'sex': 'Female'}}

# How would you add Bob Flint age 35 male?

people['Bob2'] = {'first': 'Bob', 'last': 'Flint', 'age': '35', 'sex': 'Male'}


# How would you get the length of people?

len(people)


# Create a dictionary from the CSV file 'people.csv'

skipped


# List comprehension review:
#[<expression> for <item> in <sequence> if <condition>] 
# Create a new list of squares for numbers ranging from 0 to 10

new_list = [num ** 2 for num in range(11)]

new_list = []
for num in range(11):
    new_list.append(num ** 2)


# Use dictionary comprehension to solve this problem:
# dict_variable = {key:value for (key,value) in dictonary.items() if condition}
# Double each value in the following: 
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

new_dict = {key:value*2 for (key, value) in dict1.items()}


# create a new dictionary where the key is a number divisible
# by 2 in a range of 0-10 and it's value is the square of the number.

# we want: dictionary = {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

dictionary = {num: num ** 2 for num in range(11) if num % 2 == 0 }


