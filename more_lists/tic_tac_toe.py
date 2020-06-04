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



def game_board(length=3):
    grid = []
    for i in range(length):
        row = []
        grid.append(row)
        for j in range(length):
            row.append("_")
    return grid


def display_board(grid):
    for row in grid:
        print(row)


def update_position(grid, row, col, player):
    grid[row][col] = player


def get_player_move(board, player):
    valid = False
    while not valid:
        row = int(input(f"Player {player}, enter row: "))
        col = int(input(f"Player {player}, enter col: "))
        if not valid_move(board, row, col):
            print("Invalid move, try again")
    return row, col

def valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != "_":
        return False
    return True


def tie(grid):
    for row in grid:
        for col in row:
            if "_" == col:
                return False
    return True


def game_over(board):
    return three_in_row_horizontal(board) or three_in_row_vertical(board) or three_in_row_diagonal_up(board) or three_in_row_diagonal_down(board)

def three_in_row_horizontal(grid):
    for row in grid:
        if len(set(row)) == 1 and "_" not in row:
            return True
    return False

def flip_grid(grid):
    flipped_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid)):
            new_row.append(grid[j][i])
        flipped_grid.append(new_row)
    return flipped_grid

def three_in_row_vertical(grid):
    flipped_grid = flip_grid(grid)
    return three_in_row_horizontal(flipped_grid)


def three_in_row_diagonal_down(grid):
    lst = []
    for row in range(len(grid)):
        lst.append(grid[row][row])
    if len(set(lst)) == 1 and lst[0] != "_":
        return True
    return False


def three_in_row_diagonal_up(grid):
    lst = []
    lst.append(grid[0][2])
    lst.append(grid[1][1])
    lst.append(grid[2][0])
    if len(set(lst)) == 1 and lst[0] != "_":
        return True
    return False
            

def change_players(player):
    if player == "O":
        player = "X"
    else:
        player = "O"
    return player

def main():
    clear()
    board = game_board()
    display_board(board)
    player = "O"
    while not tie(board) and not game_over(board):
        player = change_players(player)
        row, col = get_player_move(board, player)
        update_position(board, row, col, player)
        clear()
        display_board(board)
    if tie(board):
        print("It's a tie!")
    if game_over(board):
        print(f"Player {player} wins!")

if __name__ == "__main__":
    main()