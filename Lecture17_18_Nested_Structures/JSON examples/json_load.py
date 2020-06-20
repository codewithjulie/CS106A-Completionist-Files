import json

def main():
    # Open and load json file into a python variable
    with open('load.json') as file:
        ages = json.load(file)
        for key, value in ages.items():
            print(key, value)


if __name__ == "__main__":
    main()


