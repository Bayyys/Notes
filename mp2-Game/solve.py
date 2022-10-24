# -*- coding: utf-8 -*-


import imp


def solve(board, pents):
    """
    This is the function you will implement. It will take in a numpy array of the board
    as well as a list of n tiles in the form of numpy arrays. The solution returned
    is of the form [(p1, (row1, col1))...(pn,  (rown, coln))]
    where pi is a tile (may be rotated or flipped), and (rowi, coli) is 
    the coordinate of the upper left corner of pi in the board (lowest row and column index 
    that the tile covers).
    
    -Use np.flip and np.rot90 to manipulate pentominos.
    
    -You may assume there will always be a solution.
    """

    import numpy as np
    from Pentomino import get_pent_idx, is_pentomino, add_pentomino, remove_pentomino, check_correctness

    def add_pentomino(board, pent, coord):
        """
        Adds a pentomino pent to the board. The pentomino will be placed such that
        coord[0] is the lowest row index of the pent and coord[1] is the lowest
        column index.
        """
        for row in range(pent.shape[0]):
            for col in range(pent.shape[1]):
                if pent[row][col] != 0:
                    if (coord[0] + row >= board.shape[0]) or (coord[1] + col >= board.shape[1]) or (board[coord[0] + row][coord[1] + col] != 0):  # Overlap
                        return False
                    else:
                        board[coord[0] + row][coord[1] + col] = pent[row][col]
        return True

    num_solve = 0
    visited = [0] * len(pents)
    sol_board = np.zeros(board.shape)

    for i in range(sol_board.shape[0]):
        for j in range(sol_board.shape[1]):
            if board[i][j] == 0:
                sol_board[i][j] = -1

    def solve_helper(board, pents, sol_list, visited):
        nonlocal num_solve
        if len(sol_list) == len(pents):
            # num_solve += 1
            return sol_list
        for i in range(len(pents)):
            if visited[i] == 1:
                continue
            for flipnum in range(3):
                p = np.copy(pents[i])
                if flipnum > 0:
                    p = np.flip(pents[i], flipnum-1)
                for rot_num in range(4):
                    for row in range(board.shape[0]):
                        for col in range(board.shape[1]):
                            board_copy = np.copy(board)
                            if add_pentomino(board_copy, p, (row, col)):
                                board = board_copy
                                visited[i] = 1
                                sol_list.append((p, (row, col)))
                                sol = solve_helper(board, pents, sol_list, visited)
                                if sol is not None:
                                    return sol
                                visited[i] = 0
                                sol_list.pop()
                                remove_pentomino(board, i)
                    p = np.rot90(p)
        return None

    def CSP(board, pents, sol_list, visited):
        if len(sol_list) == len(pents):
            return sol_list
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if board[i][j] == 0:
                    for k in range(len(pents)):
                        if visited[k] == 1:
                            continue
                        for flipnum in range(2):
                            p = np.copy(pents[k])
                            if flipnum > 0:
                                p = np.flip(pents[k], flipnum-1)
                            for rot_num in range(4):
                                board_copy = np.copy(board)
                                if add_pentomino(board_copy, p, (i, j)) and board_copy[i][j] != 0:
                                    board = board_copy
                                    # print(board)
                                    visited[k] = 1
                                    sol_list.append((p, (i, j)))
                                    sol = CSP(board, pents, sol_list, visited)
                                    if sol is not None:
                                        print(board)
                                        return sol
                                    visited[k] = 0
                                    sol_list.pop()
                                    remove_pentomino(board, k)
                                p = np.rot90(p)
                    return None


    # sol_list = solve_helper(sol_board, pents, [], visited)
    # print(sol_board)
    # print(pents)
    sol_list = CSP(sol_board, pents, [], visited)
    print(sol_list)
    
    if sol_list is None:
        return NotImplementedError
    else:
        return sol_list