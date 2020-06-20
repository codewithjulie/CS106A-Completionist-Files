import json
import tkinter
import time
import math

START_YEAR = 1800
END_YEAR = 2015
N_YEARS = END_YEAR - START_YEAR + 1
MAX_LIFE = 90
MIN_LIFE = 20
MAX_GDP = math.log(100000)
MIN_GDP = math.log(500)

# related to drawing
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
X_AXIS_OFFSET = 50
Y_AXIS_OFFSET = 50

'''
Assumes that mindset.json stores the data as a giant dictionary.
The dictionary associates years with all data for that year. 

Each year is a dictionary from country name to country data. For example:

{
    "1800":{
        "Afghanistan":{"life":28.21, "pop":3280000, "gdp":603.0},
        "Albania":{"life":28.2, "pop":3284351, "gdp":604.0},
        ...
        "Zimbabwe":{"life":20.8, "pop": 12226542, "gdp":98.0}
    },

    ...
}
'''

def main():
    data = json.load(open('mindset.json'))
    track_country = input('Country to track: ')

    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Mindset')
    # for each year to be visualized
    for year in range(START_YEAR, END_YEAR + 1):
        # draw the current year
        clear_canvas(canvas)
        draw_graph_background(canvas)
        draw_year_text(canvas, year)

        year_data = data[str(year)]
        plot_year_bubbles(canvas, year_data, track_country)
        

        # animate
        canvas.update()
        time.sleep(1/50)
    canvas.mainloop()

def plot_year_bubbles(canvas, year_data, track_country):
    for country_name in year_data:
        country_data = year_data[country_name]
        life = country_data['life']
        pop = country_data['pop']
        gdp = country_data['gdp']
        filled = country_name == track_country
        draw_bubble(canvas, life, gdp, pop, filled)

#**************************************************************
#                      Helper Functions                       *
#**************************************************************

def draw_bubble(canvas, life, gdp, pop, filled):
    r = math.sqrt(pop) / 700
    plot_width = CANVAS_WIDTH - Y_AXIS_OFFSET
    plot_height = CANVAS_HEIGHT - X_AXIS_OFFSET
    log_gdp = math.log(gdp)

    x = scale(log_gdp, MAX_GDP, MIN_GDP, plot_width) + Y_AXIS_OFFSET
    y = scale(life, MAX_LIFE, MIN_LIFE, plot_height) + X_AXIS_OFFSET
    y = CANVAS_HEIGHT - y
    # y = min(y, CANVAS_HEIGHT - X_AXIS_OFFSET)
    make_centered_bubble(canvas, x, y, 2 * r, filled)

def draw_year_text(canvas, year):
    y = CANVAS_HEIGHT - X_AXIS_OFFSET - 100
    canvas.create_text(380, y, anchor='c', font='Times 24', text=str(year))

def clear_canvas(canvas):
    canvas.delete('all')

#**************************************************************
#           PRIVATE!!! trespassers will be prosecuted         *
#**************************************************************

def scale(v, max_v, min_v, screen_max):
    p = (v - min_v) / (max_v - min_v)
    p = max(0, p)
    return p * screen_max 

def make_centered_bubble(canvas, center_x, center_y, size, filled):
    x_1 = center_x - size/2
    y_1 = center_y - size/2
    fill = None
    if filled:
        fill = 'red'
    canvas.create_oval(x_1, y_1, x_1 + size, y_1 + size, fill=fill)
    
def draw_graph_background(canvas):
    draw_x_axis(canvas)
    draw_y_axis(canvas)
    
def draw_x_axis(canvas):
    y = CANVAS_HEIGHT - X_AXIS_OFFSET
    canvas.create_line(0, y, CANVAS_WIDTH, y)

    label_y = y + X_AXIS_OFFSET/2
    x_axis_txt = "GDP (adjusted log $)"
    canvas.create_text(380, label_y, anchor='c', font='Times 24', text=x_axis_txt)
    
def draw_y_axis(canvas):
    canvas.create_line(Y_AXIS_OFFSET, 0, Y_AXIS_OFFSET, CANVAS_HEIGHT)

    y_axis_txt = "Life Expectancy (years)"
    canvas.create_text(Y_AXIS_OFFSET/2, 300, anchor='c', font='Times 24', text=y_axis_txt, angle=90)

def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas




if __name__ == '__main__':
    main()