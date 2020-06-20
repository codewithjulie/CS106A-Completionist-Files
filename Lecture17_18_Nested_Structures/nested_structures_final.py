# Dictionaries:
Unordered, key-value pairs, keys must be hashable
Cannot look up keys by using value


# Creating a dictionary:
dictionary = {}

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

ages = {
    'Bob': 40
    'Mary': 35
    'John': 30
}

ages = dict[('Bob', 40), ('Mary', 35), ('John', 30)]
numbers = dict(one=1, two=2, three=3)
people = dict([['Bob', 40], ['Mary', 35], ['John', 30]])


# Accessing a dictionary:
ages['Bob']         # 40
ages['Santa']       # KeyError
ages['John'] = 21   # Updates John's value to 21
ages['John']        # 21
ages['John'] += 3   # Updates John's value to 24
ages[30]            # KeyError, cannot look up keys using values


# Looping through dictionary:
for key in dictionary:
    value = dictionary[key]
    print(key, value)


# Reverse dictionary problem
ages = {
    'Mehran':50,
    'Gary':70,
    'Chris':32,
    'Brahm':23,
    'Adele':32,
    'Lionel':32,
    'Rihanna':32,
    'Stephen':32,
    'Skrillex':32
}


# Creating a dictionary in a dictionary
dictionary = {}
dictionary['John'] = {}
dictionary['John']['first'] = 'John'
dictionary['John']['last'] = 'Doe'


# Accessing a dictionary in a dictionary
people = {'John': {'first': 'John', 'last': 'Doe', 'age': '27', 'sex': 'Male'},
          'Mary': {'first': 'Mary', 'last': 'Smith', 'age': '22', 'sex': 'Female'},
          'Bob': {'first': 'Bob', 'last': 'Flint', 'age': '32', 'sex': 'Male'}}

for person in people:
    print(people[person]['age'])


# How would you access the 27?
people['John']['age']

# How would you print all the values for first?
for person in people:
    print(people[person]['first'])

# How would you get the keys for everyone who is male?
for person in people:
    if people[person]['sex'] == 'Male':
        print(person)

# How would you add Bob Flint age 35 male?
people['Bob'] = {'first': 'Bob', 'last': 'Flint', 'age': 35, 'sex': 'Male'}

# How would you get the length of people?
len(people)

# How would you get the length of 'John'?
len(people['John'])


# How to create a nested dictionary from a CSV file
people = {}

with open('people.csv') as file:
    # first, last, age, sex
    first_line = file.readline().strip().split(',')
    for data in file:
        data = data.strip().split(',')
        name = data[0]
        for i in range(len(data)):
            if name not in people:
                people[name] = {}
            people[name][first_line[i]] = data[i]

print(people)


# Shortened by using dictionary comprehension
dictionary = {}

with open('people.csv') as file:
    header = file.readline().strip().split(',')
    
    for line in file:
        line = line.strip().split(',')
        first, last, age, sex = line[0], line[1], line[2], line[3]
        dictionary[first] = {header[i]:line[i] for i in range(len(line))} # Dictionary comprehension