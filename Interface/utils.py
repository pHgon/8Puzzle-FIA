import numpy as np
import time
import os
from random import shuffle

def swap_position(board, indexes):
    zero_pos = find_ij(board)

    board[zero_pos[0]][zero_pos[1]] = board[indexes[0]][indexes[1]]
    board[indexes[0]][indexes[1]] = 0

    return board


# Retorna uma Lista com os possiveis vizinhos do 0
def get_neighbors(board, nmax):
    zero_pos = []
    neighbors_list = []
    for i in range(0, nmax):
        for j in range(0, nmax):
            if board[i][j] == 0:
                zero_pos = [i, j]

    i, j = zero_pos[0], zero_pos[1]
    if i-1 >= 0:
        neighbors_list.append([i-1,j])
    if i+1 < nmax:
        neighbors_list.append([i+1,j])
    if j-1 >=0:
        neighbors_list.append([i,j-1])
    if j+1 < nmax:
        neighbors_list.append([i,j+1])

    return neighbors_list


# Retorna uma Lista com os possiveis vizinhos do 0, em ordem embaralhada
def get_random_neighbors(board, nmax):
    zero_pos = []
    neighbors_list = []
    for i in range(0, nmax):
        for j in range(0, nmax):
            if board[i][j] == 0:
                zero_pos = [i, j]

    i, j = zero_pos[0], zero_pos[1]
    if i-1 >= 0:
        neighbors_list.append([i-1,j])
    if i+1 < nmax:
        neighbors_list.append([i+1,j])
    if j-1 >=0:
        neighbors_list.append([i,j-1])
    if j+1 < nmax:
        neighbors_list.append([i,j+1])

    shuffle(neighbors_list)

    return neighbors_list


def find_ij(board):
    for i in range(0, np.shape(board)[0]):
        for j in range(0, np.shape(board)[1]):
            if board[i][j] == 0:
                return [i,j]


# @param n = dimensao da matriz nxn
# Retorna a matriz correta
def create_sorted_matrix(n):
    matrix = np.zeros((n, n))
    count = 1
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = count
            count += 1
    matrix[n-1][n-1] = 0
    return matrix

# @param board = matriz
# @param n = dimensao da matriz
# @return
def manhattan_heuristic(board, n):
    sorted = create_sorted_matrix(n)
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            temp = board[i][j]
            for k in range(0, n):
                for l in range(0, n):
                    if board[i][j] == sorted[k][l]:
                        count += abs(k-i) + abs(l-j)
    return count


# @param board = matriz
# @param n = dimensao da matriz
def diff_heuristic(board, n):
    sorted = create_sorted_matrix(n)
    diff_itens = 0
    for i in range(0, n):
        for j in range(0, n):
            if board[i][j] != sorted[i][j]:
                diff_itens += 1
    return diff_itens


# @param board = matriz
# @param n = dimensao da matriz
# @return
def chessboard_heuristic(board, n):
    sorted = create_sorted_matrix(n)
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            temp = board[i][j]
            for k in range(0, n):
                for l in range(0, n):
                    if board[i][j] == sorted[k][l]:
                        count += max([abs(k-i), abs(l-j)])
    return count

def get_solution(curr_node):
    solution = []
    while (curr_node.get_value() != -1):
        solution.append(int(curr_node.get_value()))
        curr_node = curr_node.get_upper()
    return list(reversed(solution))