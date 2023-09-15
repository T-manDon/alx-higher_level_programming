#!/usr/bin/python3
"""N-Queens Problem Solver Module
This module includes functions to search for solutions to the N-Queens puzzle.
"""
def all_possible(n=4):
    """Find all possible solutions to the N-Queens puzzle for a board of size n x n.

    Args:
        n (int, optional): The size of the board. Defaults to 4.
    """
    for x in range(n):
        matrix = []
        matrix.append([0, x])
        col = [z for z in range(n)]
        col.remove(x)
        explore_solutions(matrix, 1, col, n)


def explore_solutions(matrix, row, col, n):
    """Explore solutions to the N-Queens puzzle through a recursive backtracking algorithm.

    Args:
        matrix (list of list): A list of lists representing queen positions on the board.
        row (list): A list of possible row positions for remaining queens.
        col (list): A list of possible column positions for remaining queens.
        n (int): The board size and number of queens.
    """
    if len(matrix) is n:
        return matrix

    if row:
        x = row
        for y in col:
            if (not queens_bottom_right(matrix, x + 1, y + 1, n) or
                not queens_bottom_left(matrix, x + 1, y - 1, n) or
                not queens_top_left(matrix, x - 1, y - 1, n) or
                not queens_top_right(matrix, x - 1, y + 1, n)):
                continue
            matrix.append([x, y])
            new_col = list(col)
            new_col.remove(y)
            new_matrix = explore_solutions(matrix, row + 1, new_col, n)
            if new_matrix is not None:
                print(matrix)
            matrix.remove([x, y])
    return None


def queens_bottom_right(matrix, y, x, n):
    """Check if there are queens on the bottom right diagonal of a position.

    Args:
        matrix (list of list): A matrix representing queen positions on the board.
        y (int): Row or y-coordinate.
        x (int): Column or x-coordinate.
        n (int): The board size.

    Returns:
        bool: True if no queens exist on the bottom right diagonal of the given position, otherwise False.
    """
    while y < n and x < n:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x += 1
    return True


def queens_bottom_left(matrix, y, x, n):
    """Check if there are queens on the bottom left diagonal of a position.

    Args:
        matrix (list of list): A matrix representing queen positions on the board.
        y (int): Row or y-coordinate.
        x (int): Column or x-coordinate.
        n (int): The board size.

    Returns:
        bool: True if no queens exist on the bottom left diagonal of the given position, otherwise False.
    """
    while y < n and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x -= 1
    return True


def queens_top_left(matrix, y, x, n):
    """Check if there are queens on the top left diagonal of a position.

    Args:
        matrix (list of list): A matrix representing queen positions on the board.
        y (int): Row or y-coordinate.
        x (int): Column or x-coordinate.
        n (int): The board size.

    Returns:
        bool: True if no queens exist on the top left diagonal of the given position, otherwise False.
    """
    while y >= 0 and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x -= 1
    return True


def queens_top_right(matrix, y, x, n):
    """Check if there are queens on the top right diagonal of a position.

    Args:
        matrix (list of list): A matrix representing queen positions on the board.
        y (int): Row or y-coordinate.
        x (int): Column or x-coordinate.
        n (int): The board size.

    Returns:
        bool: True if no queens exist on the top right diagonal of the given position, otherwise False.
    """
    while y >= 0 and x < n:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x += 1
    return True


if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    all_possible(n)
