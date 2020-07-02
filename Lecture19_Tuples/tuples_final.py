# What is a tuple?
immutable
ordered
()
collection of items
coordinate (x, y)
rgb (r, g, b)



# Creating a tuple, are these valid ways of creating a tuple?
my_tuple = (1, 2, 3)
empty_tuple = ()
one_tuple = (1) == one_tuple = 1
one_tuple = (1,)
random_tuple = (2.5, 'red', 3, [4, 'g'])


# Tuple functions
letters = ('a', 'g', 'c', 'z', 't')

len(letters)            # 5
letters[3] = 'h'        # Error
letters.sort()          # 
sorted(letters)         # ['a', 'c', 'g', 't', 'z']
'c' in letters          # True
'z' not in letters      # False
min(letters)            # a
max(letters)            # z
letters.pop()           # AttributeError
letters.append('A')     # AttributeError
sum(letters)            # TypeError
sum(1, 2, 3, 4, 5)      # Error
list(letters)           # ['a', 'g', 'c', 'z', 't']



# Access elements of Tuple, slicing
Very much like lists - for sake of time, refer to lists lecture


# Assignment with tuples
(x, y) = (3, 4)
x, y = 3, 4
x = 3, 4
y = 3,

def multiple_returns():
    return (5, 6, 7)

x, y, z = multiple_returns()


# How to get list of tuple pairs from dictionary?
dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

[('a', 1), ('b', 2), ('c', 3)]

lst = []
for key, value in dictionary.items():
    lst.append((key,value))

Comprehension
lst = [(key, value) for key, value in dictionary.items()]


list(dictionary.items())


# Remember this? (key, value is a tuple)
for key, value in dictionary.items()



# What is the difference between a method and a function?
lst.sort() vs sorted(lst)



# Basic sorting
nums = (8, 42, 4, 8, 15, 16)
sorted(nums)            # 
nums                    # 

fruits = ('strawberries', 'apricots', 'plums', 'Peaches')

sorted(fruits)          # 
ord('A')                # 65
chr(65)                 # 'A'


# Intermediate sorting
nums = (8, 42, 4, 8, 15, 16)
sorted(nums, reverse=True)          # 


# Advanced sorting - using a custom function
optional parameter: key=function name       # No parentheses

fruits = ('apples', 'pears', 'Peaches', 'strawberries')

sorted(fruits, key=str.lower)           # Doesn't actually change the string
sorted(fruits, key=len)


# Super deluxe advanced sorting - list of tuples
def get_count(ages):
    return ages[1]

def main():
    ages = [['John', 50], ['Mary', 25], ['Bob', 30]]  # Can be pairs of tuples or lists
    sort_names = sorted(ages)
    print(sort_names)
    sort_count = sorted(ages, key=get_count(ages))      # we have to accept no () ...
    print(sort_count)
    rev_sort_count = sorted(ages, key=lambda ages: ages[1])
    print(rev_sort_count)

look into this more to be able to explain it
lambda a: a ** 2

students = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

