# What are the characteristics of a dictionary?
mutable, keys can be : immutable data types, unordered

# How do we create a dictionary?
dictionary = {}
dictionary = {2:4, 3:9, 4:16}


numbers = dict(one=1, two=2, three=3)
people = dict([['Bob', 40], ['Mary', 35], ['John', 30]])


# Accessing a dictionary:
people['Bob']             # 
people['Santa']           # 
people['John'] = 21       # 
people['John']            # 
people['John'] += 3       # 
people[30]                # 


# How can I print key value pairs in people?
for key, value in people.items():
    print(key)


# How can you get all keys or all values?



# Go to reverse dictionary problem: reverse_map.py



# Dictionaries in a dictionary
people = {'John': {'first': 'John', 'last': 'Doe', 'age': '27', 'sex': 'Male'},
          'Mary': {'first': 'Mary', 'last': 'Smith', 'age': '22', 'sex': 'Female'}}


# How would you access the 27?



# How would you print all the values for first?



# How would you get the keys for everyone who is male?



# How would you add Bob Flint age 35 male?



# How would you get the length of people?
len(people) == 2



# How would you get the length of 'John'?
len(people['John']) == 4



# Create a dictionary from the CSV file 'people.csv'



