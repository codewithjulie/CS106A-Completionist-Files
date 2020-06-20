import json

'''
Allows the user to navigate around a (text based) world.
Data comes from adventure.json
'''
START = 'haunted mansion'

def main():
	data = json.load(open('adventure.json'))
	play_game(data)


def play_game(data):
    print('Welcome to the Haunted Mansion Game:\n')
    current_room = START

    while True:
        print("\n", data[current_room]['text'])
        if current_room == 'escape' or current_room == 'closet':
            break
        moves = data[current_room]['moves']
        for keys, values in moves.items():
            print("   ", keys, ":", values)
        direction = input("What is your move? ")
        current_room = moves[direction]



if __name__ == '__main__':
	main()