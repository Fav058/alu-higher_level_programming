#!/usr/bin/python3
"""Solves the N queens puzzle."""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col) safely.

    Args:
        board (list): Current placement of queens (col per row).
        row (int): Row to check.
        col (int): Column to check.

    Returns:
        bool: True if placing a queen at (row, col) is safe.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively attempt to place queens row by row.

    Args:
        n (int): The size of the board.
        row (int): The current row to place a queen in.
        board (list): Current placement of queens (col per row).
        solutions (list): Accumulator for all found solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve(n, row + 1, board, solutions)
            board.pop()


def main():
    """Parse arguments, validate them, and print all solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, 0, [], solutions)
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == "__main__":
    main()
