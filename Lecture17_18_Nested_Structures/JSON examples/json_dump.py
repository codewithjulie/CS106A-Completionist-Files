import json


def main():
    data = [
        "a",
        25,
        {
            "test":"woot"
        }
    ]
    
    # How to put above data structure in a json file?
    json.dump(data, open('dumped.json', 'w'), indent=4)
    
	

if __name__ == '__main__':
	main()