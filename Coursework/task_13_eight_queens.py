"""
Task 13: Solve the 8-Queens Problem
AI Lab Coursework - Constraint Satisfaction & Backtracking Search

AI Problem Formulation:
    Place 8 queens on an 8x8 chessboard such that no two queens attack each other.
    Constraints:
      1. No two queens in the same row.
      2. No two queens in the same column.
      3. No two queens on the same diagonal.

Description:
    Implements a recursive backtracking algorithm (Constraint Satisfaction Problem)
    to find all 92 distinct solutions to the 8-Queens problem, printing board layouts.
"""

from typing import List


def is_safe(board: List[int], current_row: int, current_col: int) -> bool:
    """
    Checks if placing a queen at (current_row, current_col) is safe from
    attacks by previously placed queens in rows 0 .. current_row - 1.
    board[r] represents the column index of the queen in row r.
    """
    for r in range(current_row):
        c = board[r]
        # Same column check
        if c == current_col:
            return False
        # Diagonal check: |row1 - row2| == |col1 - col2|
        if abs(r - current_row) == abs(c - current_col):
            return False
    return True


def solve_n_queens(n: int = 8) -> List[List[int]]:
    """
    Solves the N-Queens problem via backtracking search.
    Returns all valid board configurations.
    """
    solutions: List[List[int]] = []
    board = [-1] * n

    def backtrack(row: int):
        if row == n:
            solutions.append(list(board))
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col        # Place queen
                backtrack(row + 1)      # Recurse for next row
                board[row] = -1         # Backtrack

    backtrack(0)
    return solutions


def print_board(solution: List[int]):
    """Pretty prints the chessboard configuration."""
    n = len(solution)
    print("  +" + "---+" * n)
    for row in range(n):
        row_str = "  |"
        for col in range(n):
            if solution[row] == col:
                row_str += " Q |"
            else:
                row_str += " . |"
        print(row_str)
        print("  +" + "---+" * n)


def main():
    print("=" * 60)
    print("Task 13: 8-Queens Problem (Backtracking / CSP)")
    print("=" * 60)

    n = 8
    solutions = solve_n_queens(n)
    print(f"Total valid non-attacking configurations for {n}-Queens: {len(solutions)}")

    # Display the first 2 solutions visually
    num_to_display = 2
    for idx in range(num_to_display):
        print(f"\nSolution #{idx + 1} (Queen column positions per row: {solutions[idx]}):")
        print_board(solutions[idx])


if __name__ == "__main__":
    main()

