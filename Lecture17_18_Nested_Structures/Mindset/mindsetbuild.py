"""{"1800": {"Afghanistan": {"gdp": 603.0, "life": 28.21, "pop": 3280000.0}}}"""

import json


GDP_FILE = 'gdp.csv'
LIFE_FILE = 'life.csv'
POP_FILE = 'pop.csv'


def main():
    # Create dictionary
    data = {}
    
    # Add data from file
    add_data(GDP_FILE, data)
    add_data(POP_FILE, data)
    add_data(LIFE_FILE, data)

    # Dump dictionary into json file
    json.dump(data, open('mindset_build.json', 'w'))


def add_data(filename, data):
    name = filename.split(',')[0] # ex. pop.csv - pop
    with open(filename) as file:
        for line in file:
            line = line.strip().split(',')
            country = line[0]
            details = line[1:]
            for i in range(len(details)):
                year = i + 1800
                if year not in data:   # The line we were missing to make it work
                    data[year] = {}
                if country not in data[year]:
                    data[year][country] = {}
                data[year][country][name] = details[i]
    

if __name__ == "__main__":
    main()