
from pprint import pprint

def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not filles yet --> rep with -1
    #return row, col tuple (or(None, None) if there is none)

    #use 0-8 for indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None # if there aren't any empty spaces

def is_valid(puzzle, guess, row, col):
    #figure out whether the guess at the row/col of the column is a valid guess
    #returns a Boolean

    #valid guess == Number must'nt be repeated in the row column or 3x3 square that it appears in 
    #row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False #if we've repeated then guess is invalid
    
    #column
    #col_vals = []
    #for i in range(9):
    #    col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    #solve sudoku using Backtracking
    #the puzzle is a list of lists, where each inner list is a row in the puzzle
    #return whether a solution exists 
    #mutates puzzle to be the solution 

    #1. Choose somewhere to make a guess
    row, col = find_next_empty(puzzle)

    #1(b). If there's no spot left, then done bcoz only valid inputs are allowed
    if row is None: #true if find_next_empty returns None, None
        return True
    
    #2. If there's a spot then make a guess btn 1-9
    for guess in range(1, 10):
        #3. Check if guess is valid
        if is_valid(puzzle, guess, row, col):
            #3(b). If guess is valid then place at spot
            puzzle[row][col] = guess
            #4. Recursively call solver 
            if solve_sudoku(puzzle):
                return True
            
            #5. If not valid or if nothing gets returned true, backtrack and try new number 
            puzzle[row][col] = -1

    #6. If none of the numbers work then puzzle is unsolvable
    return False 
    
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)