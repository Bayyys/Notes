# -*- coding: utf-8 -*-
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
    """
    算法思路：遍历需要填充的每一个空格，然后遍历所有的pents，如果pent可以填充到该空格，则将该pent填充到该空格，然后递归调用solve函数，直到所有的空格都被填充。
    算法创新：1. 在遍历pents前，先对所有的pents进行翻转和旋转，将所有形态进行存储，以可以减少遍历的次数；
            2. 填充pent时，将pent的有效块与board的空格进行对齐，避免pent填充遗漏；
            3. 以board的空格为基准，遍历所有的空格，避免填充过程产生不可填充的部分；
            4. 在填充pent时，先判断pent是否已经被填充，如果已经被填充，则跳过该pent，避免重复填充。
    """

    import numpy as np
    from Pentomino import get_pent_idx, is_pentomino, add_pentomino, remove_pentomino, check_correctness

    def all_pents(pents):
        """
        Returns a list of all possible pentominos (including rotations and flips)
        """
        all_pents = [[] for x in range(1, len(pents) + 1)]
        count = 0
        for pent in pents:
            shape = []
            for flipnum in range(3):
                p = np.copy(pent)
                if flipnum > 0:
                    p = np.flip(pent, flipnum-1)
                for rot_num in range(4):
                    if p.tolist() in shape:
                        continue
                    shape.append(p.tolist())
                    all_pents[count].append(p)
                    p = np.rot90(p)
            count += 1
        return all_pents

    def fallback(pent):
        """
        Returns the number of pent tiles that are not covered
        """
        for col in range(pent.shape[1]):
            if pent[0][col] != 0:
                return col

    def add_pentomino(board, pent, coord):
        """
        Adds a pentomino pent to the board. The pentomino will be placed such that
        coord[0] is the lowest row index of the pent and coord[1] is the lowest
        column index.
        """
        if coord[1] < 0:
            # If the pentomino is out of bounds, move it back in
            return False
        for row in range(pent.shape[0]):
            for col in range(pent.shape[1]):
                if pent[row][col] != 0:
                    # If the tile is not empty
                    if (coord[0] + row >= board.shape[0]) or (coord[1] + col >= board.shape[1]) or (
                            board[coord[0] + row][coord[1] + col] != 0):  # Overlap
                        return False
                    else:
                        board[coord[0] + row][coord[1] + col] = pent[row][col]
        return True

    def CSP(board, pents, sol_list, visited):
        if len(sol_list) == len(pents):
            # 所有的pent都放好了
            return sol_list
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if board[i][j] == 0:    # 找到第一个空格
                    for k in range(len(pents)):  # 遍历所有的pent
                        if visited[k] == 1:
                            # 如果这个pent已经放好了
                            continue
                        for pent in all_pents[k]:   # 遍历这个pent的所有形态
                            board_copy = np.copy(board)  # 复制一份board
                            back = fallback(pent)   # 找到这个pent的fallback
                            if add_pentomino(board_copy, pent, (i, j - back)) and board_copy[i][j] != 0:
                                # 如果这个pent能放在这个位置
                                board = board_copy  # 更新board
                                visited[k] = 1  # 标记这个pent已经放好了
                                sol_list.append((pent, (i, j - back)))  # 把这个pent加入sol_list
                                sol = CSP(board, pents, sol_list, visited)  # 递归
                                if sol is not None:
                                    # 如果找到了解
                                    return sol
                                visited[k] = 0  # 如果没找到解，把这个pent标记为没放好
                                sol_list.pop()  # 把这个pent从sol_list里删掉
                                remove_pentomino(board, k)  # 把这个pent从board里删掉
                    return None

    all_pents = all_pents(pents)    # 所有的pent的所有形态
    visited = [0] * len(pents)  # 标记pent是否已经放好
    sol_list = None  # 存放解
    sol_board = np.zeros(board.shape)   # 存放解的board


    for i in range(sol_board.shape[0]):
        for j in range(sol_board.shape[1]):
            if board[i][j] == 0:
                sol_board[i][j] = -1    # 把board里的空格标记为-1

    sol_list = CSP(sol_board, pents, [], visited)   # 调用CSP

    if sol_list is None:
        return []
    else:
        return sol_list
