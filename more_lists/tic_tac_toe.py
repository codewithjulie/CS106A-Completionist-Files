"""
File - 'tic_tac_toe.py'
----------------------------
Milestones:
1. Create a board (3 x 3 grid)
2. Player takes turns
3. Where to put it?
4. Check valid move
5. Place the marker
6. Determine winner
7. Determine tie
. 
"""

import os
clear = lambda: os.system('clear')

# Create board (3 x 3 grid)
def game_board(length=3):
    grid = []
    for i in range(length):
        row = []
        grid.append(row)
        for j in range(length):
            row.append("_")
    return grid


# Print the board to terminal
def display_board(grid):
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
        row = int(input(f"Player {player}, enter row: "))
        col = int(input(f"Player {player}, enter col: "))
        if not valid_move(board, row, col):
            print("Invalid move, try again")
        else:
            break
    return row, col


# Check if position is within the grid and not marked
def valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != "_":
        return False
    return True


# Mark the board
def update_position(grid, row, col, player):
    grid[row][col] = player


# Determine if the game is over
def game_over(board):
    return three_in_row_horizontal(board) or \
        three_in_row_vertical(board) or \
            three_in_row_diagonal_up(board) or \
                three_in_row_diagonal_down(board) or \
                    tie(board)


# Helper method to determine if there is a tie
def tie(grid):
    for row in grid:
        for col in row:
            if "_" == col:
                return False
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

def main():
    clear()     # Start with a empty terminal
    board = game_board()
    display_board(board)
    player = "X"
    while not game_over(board):
        row, col = get_player_move(board, player)
        update_position(board, row, col, player)
        clear()
        display_board(board)
        if tie(board):
            print("It's a tie!")
        if game_over(board):
            print(f"Player {player} wins!")
        player = change_players(player)

if __name__ == "__main__":
    main()
    