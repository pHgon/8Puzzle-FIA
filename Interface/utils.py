import numpy as np

def swap_position(board, indexes):
    # print("SWAP")
    # print board
    zero_pos = find_ij(board)

    # print board
    # print zero_pos
    # print indexes

    board[zero_pos[0]][zero_pos[1]] = board[indexes[0]][indexes[1]]
    board[indexes[0]][indexes[1]] = 0

    # print board
    # print(board)
    # print()

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

def find_ij(board):

    for i in range(0, np.shape(board)[0]):
        for j in range(0, np.shape(board)[1]):
            if board[i][j] == 0:
                return [i,j]