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
    print('Welcome to the Stanford Adventure Game:\n')
    current_room = START

    while True:
        print("\n", data[current_room]['text'])
        if data[current_room]['moves'] == []:
            break
        moves = (data[current_room]['moves'])
        print("Your choices are: ")
        for move in moves:
            value = moves[move]
            print(f"\t'{move}': {value}")
        next_move = input("Where would you like to go? ")
        current_room = data[current_room]['moves'][next_move]


if __name__ == '__main__':
	main()