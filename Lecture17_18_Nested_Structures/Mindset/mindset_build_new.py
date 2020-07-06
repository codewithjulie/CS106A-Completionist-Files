import json

START_YEAR = 1800
END_YEAR = 2015
N_YEARS = END_YEAR - START_YEAR + 1

'''
Creates a file mindset.json that stores the data as a giant dictionary.
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
    print('cleaning data...')
    data = {}
    add_data(data, 'life.csv')
    add_data(data, 'pop.csv')
    add_data(data, 'gdp.csv')

    # saves data as json file!
    json.dump(data, open('mindset.json', 'w'))

def add_data(data, file_name):
    key = file_name.split('.')[0]
    for line in open(file_name):
        line = line.strip()
        line = line.split(',')
        country = line[0]
        values = line[1:]
        for i in range(N_YEARS):
            year = START_YEAR + i
            if year not in data:
                data[year] = {}
            if country not in data[year]:
                data[year][country] = {}
            data[year][country][key] = float(values[i])


if __name__ == '__main__':
    main()