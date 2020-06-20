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
    '''
    The file_name is of the format <key>.txt where
    key is one of "life", "pop", "gdp"

    Each file is a list of rows formatted like:
    Afghanistan,28.21,28.2,28.1 ...

    '''
    key = file_name.split('.')[0]
    for line in open(file_name):
        line = line.strip()
        # ['Afghanistan', '28.21', ... ]
        parts = line.split(',')

        country = parts[0]
        for i in range(N_YEARS):
            value = float(parts[i + 1])
            year = START_YEAR + i
            print(country, year, key, value)

            if not year in data:
                data[year] = {}

            if not country in data[year]:
                data[year][country] = {}

            data[year][country][key] = value



if __name__ == '__main__':
    main()