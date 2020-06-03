# How to open a file, does not close
# Per Mehran the garbage collector will close it for you
# But this might not happen with older version of Python
file = open('filename.txt')
    
for line in file:
    print(line)           # Prints each line including whitespace
    print(line.strip())   # This removes whitespace and \n


#How to open a file and automatically close it (the proper way)
with open('filename.txt') as file:  # Notice the colon, remaining code must be indented
    for line in file:
        print(line)
    print(file.readline())      # .readline returns a string and only one line
    print(file.readline(10))    # takes in an argument, prints 10 characters of line
    print(file.readlines())     # .readlines() returns a list of all lines
    print(list(file))           # same as file.readlines()


# Can take in another argument 'mode':
with open('states_us.csv', 'r') as f: # r for read, w for write, a for append
    for line in f:
        print(line)               # This prints with whitespace
        values = line.split(' ')  # Values is assigned to a list containing words
        values = line.split(',')  # In the lecture, the words were separated by commas
        print(values[0])          # This line prints the states (two column file separated by ',')


# How to open and write in a file:
with open('filename.txt', 'w') as file:           # w for write
    file.write("I am writing in a new line\n")    # Overwrites this to our file


# How to open and write in a file without overwriting:
with open('filename.txt', 'a') as file:           # a for append
    file.write("I am not overwriting our file")   # appends to the end of the file

