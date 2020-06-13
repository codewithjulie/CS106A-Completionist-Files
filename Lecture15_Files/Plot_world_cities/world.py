import tkinter
import time

# Make the window large so that we can see more detail. 
CANVAS_WIDTH = 1400
CANVAS_HEIGHT = 1000

# The viewpoint coordinates - the min and max long and lat
MIN_LONGITUDE = -180
MAX_LONGITUDE = 190
MIN_LATITUDE = -80
MAX_LATITUDE = +100
COLOR = 'blue'

FILENAME = 'new-world-cities.txt'


def main():
    # For each city that's plotted, this count will increase by 1
    n_done = 0  

    # Create the canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'US Cities')

    # Load the file
    us_cities_data = open(FILENAME)  # Can also use "with open(FILENAME) as us_cities_data"

    # Skip the first line (header)
    next(us_cities_data)

    # Not required - I was practicing how to create a dictionary of dictionaries
    # Created a dictionary with cities for keys and a list of details
    cities = {}
    for line in us_cities_data:
        cities_list = line.strip().split(',')
        cities[cities_list[0]] = cities_list[1:]  

    # Created a dictionary inside the cities dictionary
    for key in cities:
        detailed_info = cities[key]
        cities[key] = {}
        cities[key]['State'] = detailed_info[0]
        cities[key]['Latitude'] = detailed_info[1]
        cities[key]['Longitude'] = detailed_info[2]

        # Using the nested dictionary, accessed the latitude/longitude
        latitude = float(cities[key]['Latitude'])
        longitude = float(cities[key]['Longitude'])

        # Obtain the x and y coordinates for the canvas at each city
        x = (get_x_coord(longitude))
        y = (get_y_coord(latitude))

        # Plot the city
        plot_city(canvas, x, y)
        
        # Cool bit of code that allows you to see each state form
        # n_done += 1
        # if n_done % 100 == 0:
        #     canvas.update()
        #     time.sleep(1/20)

    canvas.mainloop()


def plot_city(canvas, x, y):
    canvas.create_oval(x, y, x+2, y+2, outline=COLOR)


def get_x_coord(longitude):
    return ((CANVAS_WIDTH / (MAX_LONGITUDE - MIN_LONGITUDE)) * (longitude - MIN_LONGITUDE))


def get_y_coord(latitude):
    return (CANVAS_HEIGHT * (latitude - MAX_LATITUDE)) / (MIN_LATITUDE - MAX_LATITUDE)


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


## Code that correctly 
# input = open('worldcities.csv')

# output = open('new-world-cities.txt', 'w')

# next(input)

# for line in input:
#     line = line.strip().split(',')[:4]
#     lst = []
#     for i in range(len(line)):
#         line[i] = line[i][1:-1]
#         lst.append(line[i])

#     city = ','.join(lst)
#     output.write(city + '\n')


if __name__ == '__main__':
	main()