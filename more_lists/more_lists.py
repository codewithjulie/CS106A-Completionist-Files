# Swapping elements in a list
def swap_elements_working(alist, index1, index2):
    temp = alist[index1]
    alist[index1] = alist[index2]
    alist[index2] = temp


    # Shortcut without use of temp:
    # Either said of equal is actually a tuple, parentheses are optional
    (alist[index1], alist[index2]) = (alist[index2], alist[index1])  


# Can you understand why this is buggy?
def swap_elements_buggy(elem1, elem2):
    temp = elem1
    elem1 = elem2
    elem2 = temp
    

def main():
    my_list = [10, 20, 30]
    swap_elements_buggy(my_list[0], my_list[1])
    print(my_list)


# Slicing lists = list[start:end:step]
alist = [2, 3, 5, 7, 11, 13, 17]
alist[2:4]          # What will this return?
>>> alist           # 
alist[2:2]          # 
alist[:8]           # 
alist[3:]           # 
alist[:]            # 
alist[-3:-1]        # 
alist[1:4:-1]       # 
alist[::-1]         # 

blist = alist[:]
alist == blist      # 
alist is blist      # 


# Using for each loop with lists
for elem in alist[1::2]:
    print(elem)     # 


# To delete use del
num_list = [50, 30, 40, 60, 90, 80]
del num_list[1]
>>> num_list        #
del num_list[1:4]
>>> num_list        #


# List functions and review
alist = [6, 3, 12, 4]
alist.reverse()         #
alist.sort()            #
sorted = alist.sort()   #
alist.pop()             #
alist.pop(2)            #
alist.append(5)         # modifies alist
blist = alist + [22]    # returns new list, must be two lists
alist.extend[4, 2]      #
alist.insert(3, 50)     # Takes two arguments
alist.remove(50)     
alist.count(50)
new2 = alist.copy()     #
len(alist)              #
# some functions return None
blist = alist.sort()
# pop returns what it is popping


# Passing a list as a parameter/argument
def times_two(alist):
    # Modifies list
    for i in range(len(alist)):
        alist[i] = alist[i] * 2

nums = [1, 2, 3, 4]
print(nums)
times_two(nums)
print(nums)


def times_two_pure(alist):
    # Pure function
    doubled = []
    for item in alist:
        doubled.append(item * 2)
    return doubled              # Have to return the new list

nums2 = [1, 2, 3, 4]
this_list_doubled = times_two_pure(nums2)
print(this_list_doubled)
print(nums2)


# List comprehensions
[<expression> for <item> in <sequence> if  <condition>]  # If statement is optional

mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist]

print(yourlist)



# List quiz
What is a list?                               # Mutable, ordered, 
[5, 5, 'cheese', 2.5, {"a" : 1, "b" : 2}]     # Is this a valid list?
s[:] is s
a[:] is a
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_1 == list_2
list_1 is list_2
list_3 = list_1         # This is called aliasing, try to avoid alisasing on mutable objects
list_1[2] = 50
list_1
list_2
list_3
list_4 = list_1.copy()  # Instead you want to make a copy
list_5 = list_1[:]      # This does the same thing
alist = list_1 * 3      # 
blist = [list_1] * 3    # 
>>> alist
list_1[0] = 5
>>> alist


# Nested / 2d lists
a = [[1, 2], [3, 4], [5, 6]]                        # How to access the 4?
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']    # How would you access "z" in "baz"

# How can we create a 3 x 3 grid?
grid = []
for row in range(3):
    for col in range(3):
        grid.append(None)
print(grid)


grid = []
for row in range(3):
    new_row = []
    for col in range(3):
        new_row.append(None)
    grid.append(new_row)
print(grid)


# What could be wrong with this?
grid = ([[None] * 3] * 3)
