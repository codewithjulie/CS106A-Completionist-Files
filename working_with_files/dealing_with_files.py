# How to open a file, does not close
# Per Mehran the garbage collector will close it for you
# But this might not happen with older version of Python
file = open('filename.txt')
    
for line in file:
    print(line)             # Prints each line including whitespace
    print(line.strip())     # This removes whitespace and \n

file.close()                # Was not discussed in class, but can do this to close


#How to open a file and automatically close it (the proper way)
with open('filename.txt') as file:  # Notice the colon, remaining code must be indented
    for line in file:
        print(line)
    print(file.read())            # Returns a string of the whole file
    print(file.read(50))          # Returns a string of 50 characters from the file
    print(file.readline())        # readline returns a string and only one line
    print(file.readline(10))      # takes in an argument, prints 10 characters of line
    print(file.readlines())       # readlines() returns a list of all lines
    print(list(file))             # same as file.readlines()


# Can take in another argument 'mode':
with open('states_us.csv', 'r') as f: # r for read, w for write, a for append
    for line in f:
        print(line)               # This prints with whitespace
        values = line.split(' ')  # Values is assigned to a list containing words
        values = line.split(',')  # In the lecture, the words were separated by commas
        print(values[0])          # This line prints the states (two column file separated by ',')


# How to open and write in a file:
with open('filename.txt', 'w') as file:      # 'w' for write, if file exists it will reinitialize as empty
    file.write("I am writing a new line\n")  # You will lose any previous contents


# How to open and write in a file without overwriting:
with open('filename.txt', 'a') as file:           # a for append
    file.write("I am adding to the end of a file")   # appends to the end of the file


# How to read data and write into a different file
infile = open('reading.txt', 'r')
outfile = open('writing.txt', 'w')

for line in infile:
    outfile.write(line)
    

