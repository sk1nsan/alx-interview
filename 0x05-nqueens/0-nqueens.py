#!/usr/bin/env python3

""" N queens """

import sys


def is_valid(board, row, col):
    """ Check if a queen can be placed on board[row][col] """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board):
    """ Solve the N Queens problem using backtracking """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board)
            board[row] = -1


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if (n < 4):
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve_nqueens(n, 0, [-1] * n)
    for solution in solutions:
        print(solution)
