import numpy as np
import itertools

def is_valid(board):
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if abs(i - j) == abs(board[i] - board[j]):
                return False
    return True

def solve_eight_queens():
    for perm in itertools.permutations(range(8)):
        if is_valid(perm):
            board = np.zeros((8, 8), dtype=int)
            for row, col in enumerate(perm):
                board[row, col] = 1
            return board

solution = solve_eight_queens()
print(solution)
