# How to open a file
# Per Mehran the garbage collector will close it for you
# But this might not happen with older versions of Python
file = open('filename.txt')
for line in file:
    print(line)             # Prints each line including whitespace
    print(line.strip())     # This removes whitespace
file.close()                # Was not discussed in class, but can do this to close, may want to close if you are writing, because data could be lost


# What does this do?
f = open('poem.txt')
for line in f:
    print(line.strip())
print('-----')
for line in f:
    print(line.strip())


# How to open a file and automatically close it (the proper way)
# The below commands are not meant to run all at once
with open('mydata.txt') as file:  # Notice the colon, remaining code must be indented
    print(file.read())            # Returns a string of the whole file
    print(file.read(50))          # Returns a string of 50 characters from the file
    print(file.readline())        # readline returns a string and only one line
    print(file.readline(10))      # takes in an argument, prints 10 characters of line
    print(file.readlines())       # readlines() returns a list of all lines
    print(list(file))             # same as file.readlines()
    next(file)                    # What does this do? Returns it


# Can take in another argument 'mode':
with open('states_us.csv', 'r') as f:  # If no mode is passed, defaults to 'r'
    abrv_states = {}
    for line in f:
        line = line.strip()
        line = line.split(',')
        for i in range(len(line)):
            line[i] = line[i].strip('"')  # Must reassign line[i], this strips the double quotes
        abrv_states[line[0]] = line[1]
    print(abrv_states)


# How to open and write in a file:
with open('filename.txt', 'w') as file:      # 'w' for write, if file exists it will reinitialize as empty
    file.write("I am writing a new line\n")  # You will lose any previous contents


# How to open and write in a file without overwriting:
with open('filename.txt', 'a') as file:           # a for append
    file.write("I am adding to the end of a file")   # appends to the end of the file


# How to read data and write into a different file
reader = open('reading.txt', 'r')
writer = open('writing.txt', 'w')

for line in reader:
    writer.write(line)
    print(line, file=writer)  # This line does the same thing as 'writer.write(line)'


# What the group came up with for see_the_us.py, found in Lecture 15 codes
def main():
	# get a drawing canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'US Cities')

    with open('us-cities.txt') as something:
        next(something)
        for line in something:
            line = line.strip()
            line = line.split(',')
            # ['Akron', 'AL', '32.876425', '-87.740978']
            lat = float(line[2])
            lon = float(line[3])

            plot_one_city(canvas, lat, lon)

    canvas.mainloop()
