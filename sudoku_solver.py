# ==========================================
# CONFIGURABLE TEST CASE (Change this grid to test different puzzles!)
# 0 represents empty cells
# ==========================================
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(b):
    """Prints the 9x9 Sudoku board nicely."""
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def find_empty(b):
    """Finds the next empty cell (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(b, num, pos):
    """Checks if placing 'num' at 'pos' (row, col) is valid based on rules."""
    row, col = pos

    # 1. Check the row
    if num in b[row]:
        return False

    # 2. Check the column
    if num in [b[i][col] for i in range(9)]:
        return False

    # 3. Check the 3x3 subgrid
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(b):
    """Solves the Sudoku puzzle using Backtracking."""
    empty_cell = find_empty(b)
    
    # Base case: If there are no empty cells, the puzzle is solved!
    if not empty_cell:
        return True
    
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(b, num, (row, col)):
            # Temporarily place the number
            b[row][col] = num

            # Recursively try to solve the rest of the board
            if solve_sudoku(b):
                return True

            # If it leads to a dead end, undo the choice (Backtrack)
            b[row][col] = 0

    return False

# ==========================================
# Execution
# ==========================================
if __name__ == "__main__":
    print("--- Original Sudoku Puzzle ---")
    print_board(board)
    print("\n" + "="*27 + "\n")
    
    if solve_sudoku(board):
        print("--- Solved Sudoku Puzzle ---")
        print_board(board)
    else:
        print("No solution exists for this Sudoku puzzle.")
