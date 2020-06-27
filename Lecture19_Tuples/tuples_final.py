# What is a tuple?



# Creating a tuple, are these valid ways of creating a tuple?
my_tuple = (1, 2, 3)
empty_tuple = ()
one_tuple = (1)
random_tuple = (2.5, 'red', 3, [4, 'g'])


# Tuple functions
letters = ('a', 'g', 'c', 'z', 't')

len(letters)            # 
letters[3] = 'h'        # 
letters.sort()          # 
sorted(letters)         # 
'c' in letters          # 
'z' not in letters      # 
min(letters)            # 
max(letters)            # 
letters.pop()           # 
letters.append('A')     #
sum(letters)            # 
sum(1, 2, 3, 4, 5)      # 
list(letters)           # 



# Access elements of Tuple, slicing
Very much like lists - for sake of time, refer to lists lecture


# Assignment with tuples
(x, y) = (3, 4)
x, y = 3, 4
x = 3, 4
y = 3,



# How to get list of tuple pairs from dictionary?
dictionary = {'a':1, 'b':2, 'c':3, 'd':4}



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
ord('A')                # 
chr(65)                 # 


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
    ages = [('John', 50), ('Mary', 25), ('Bob', 30)]
    sort_names = sorted(ages)
    print(sort_names)
    sort_count = sorted(ages, key=get_count)
    print(sort_count)
    rev_sort_count = sorted(ages, key=lambda ages: ages[1], reverse=True)
    print(rev_sort_count)


students = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

