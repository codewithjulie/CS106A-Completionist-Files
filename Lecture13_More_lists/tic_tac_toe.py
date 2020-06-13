"""
File - 'tic_tac_toe.py'
----------------------------
Milestones:
1. Create and display a board (3 x 3 grid)
2. Player takes turns
3. Where to put it?
4. Check valid move (any key/ch that is not 0, 1 or 2, needs improvement (will not work on a universal grid)
5. Place the marker
6. Determine winner
7. Determine tie
8. Loop to ask the player if they want to play again 
"""

import os
clear = lambda: os.system('clear')


# Create board (3 x 3 grid) and displays it
def game_board(length=3):
    grid = []
    for i in range(length):
        row = []
        grid.append(row)
        for j in range(length):
            row.append("_")
    display_board(grid)
    return grid


# Helper method to display board terminal
def display_board(grid):
    print("You're playing tic tac toe")
    for row in grid:
        print(row)


# Determine next player
def change_players(player):
    if player == "O":
        player = "X"
    else:
        player = "O"
    return player


# Get position from player
def get_player_move(board, player):
    valid = False
    while not valid:
        row = input(f"Player {player}, enter row: ")
        col = input(f"Player {player}, enter col: ")
        if not valid_move(board, row, col):
            print("Invalid move, try again")
        else:
            break
    return int(row), int(col)


# Check if position is within the grid and not marked
def valid_move(board, row, col):
    if (row == '0' or row == '1' or row == '2') and \
        (col == '0' or col == '1' or col == '2'):
        if board[int(row)][int(col)] == "_":
            return True
    return False


# Mark the board
def update_position(grid, row, col, player):
    grid[row][col] = player


# Determine if the game is over
def game_over(board):
    return three_in_row_horizontal(board) or \
        three_in_row_vertical(board) or \
            three_in_row_diagonal_up(board) or \
                three_in_row_diagonal_down(board)


# Helper method to determine if there is a tie
def tie(grid):
    for row in grid:
        for col in row:
            if "_" == col:
                return False
    print("It's a tie!")
    return True


# Helper method to determine if a player wins horizontally
def three_in_row_horizontal(grid):
    for row in grid:
        if len(set(row)) == 1 and "_" not in row:
            return True
    return False


# Helper method to determine if a player wins vertically
def three_in_row_vertical(grid):
    flipped_grid = flip_grid(grid)
    return three_in_row_horizontal(flipped_grid)


# Helper method that transposes grid used to check vertical win
def flip_grid(grid):
    flipped_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid)):
            new_row.append(grid[j][i])
        flipped_grid.append(new_row)
    return flipped_grid


# Helper method to determine if a player wins diagonally from top left
def three_in_row_diagonal_down(grid):
    lst = []
    for row in range(len(grid)):
        lst.append(grid[row][row])
    if len(set(lst)) == 1 and lst[0] != "_":
        return True
    return False


# Helper method to determine if a player wins diagonally from bottom left
def three_in_row_diagonal_up(grid):
    lst = []
    lst.append(grid[0][2])
    lst.append(grid[1][1])
    lst.append(grid[2][0])
    if len(set(lst)) == 1 and lst[0] != "_":
        return True
    return False


# Get a position, marks the position, 
def play_round(board, player):
        row, col = get_player_move(board, player)
        update_position(board, row, col, player)
        clear()
        display_board(board)
        if game_over(board):
            print(f"Player {player} wins!")
        

def ask_play_again():
    response = input("Would you like to play again? ")
    if response.lower() == "yes" or response.lower() == "y":
        return True
    return False


def main():
    play_again = True
    while play_again:
        clear()  # Clears the terminal
        board = game_board()  # Creates and displays board
        player = "X"  # Set player to X to start

        while not game_over(board) and not tie(board):
            play_round(board, player)
            player = change_players(player)
        play_again = ask_play_again()
    print("Thank you for playing, have a nice day!")


if __name__ == "__main__":
    main()
    