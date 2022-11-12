from pprint import pprint

def nextEmpty(puzzle):
    #Find the next col and row that are empty, and return row, col or None, None
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None #If there are not spaces empty

def valid(puzzle, guess, row, col):
    #Figures out if the row, col is a valid guess
    #Following the sudoku rules, the number can't be repeated in row, col of the 3x3 square

    #See if the number is already in the row
    row_val = puzzle[row]
    if guess in row_val:
        return False
    #See if the number is already in the column
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False
    #See if the number is already in the square
    row_square = (row // 3) * 3
    col_square = (col // 3) * 3

    for r in range(row_square, row_square + 3):
        for c in range(col_square, col_square + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solveSudoku(puzzle):
    #Solve sudoku
    # 1. Choose where to make a guess
    row, col = nextEmpty(puzzle)

    if row is None: #If there is not more place empty, return None None
        return True

    # 2. Place empty, then guess a number
    for guess in range(1,10):
        #See if is a valid guess
        if valid(puzzle, guess, row, col):
            #Place number
            puzzle[row][col] = guess
            #Then we call recursively our solver
            if solveSudoku(puzzle):
                return True

        #If it's not valid, we need to backtrack and try with another number
        puzzle[row][col] = 0

    #If any of the number that we try, then the sudoku is unsolvable...

if __name__ == '__main__':
    example = [
        [8, 6, 0,   7, 9, 5,   1, 0, 4],
        [4, 5, 0,   0, 0, 0,   0, 9, 0],
        [3, 7, 0,   1, 8, 0,   6, 5, 2],

        [0, 8, 0,   0, 0, 0,   3, 0, 1],
        [0, 0, 0,   9, 0, 1,   2, 8, 0],
        [0, 0, 5,   0, 3, 0,   0, 0, 0],

        [0, 0, 8,   5, 0, 3,   0, 0, 6],
        [0, 9, 6,   4, 1, 0,   0, 0, 0],
        [0, 1, 0,   0, 0, 0,   0, 2, 0]
    ]
    #print(solveSudoku(example))
    pprint(example)

