#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import instances
from solve import solve
import time


def get_pent_idx(pent):
    """
    Returns the index of a pentomino.

    返回五联牌的索引。
    """
    pidx = 0
    for i in range(pent.shape[0]):
        for j in range(pent.shape[1]):
            if pent[i][j] != 0:
                pidx = pent[i][j]
                break
        if pidx != 0:
            break
    if pidx == 0:
        return -1
    return pidx - 1


def is_pentomino(pent, pents):
    """
    Checks if a pentomino pent is part of pents

    检查 pentomino pent 是否是 pents 的一部分。
    """
    pidx = get_pent_idx(pent)
    if pidx == -1:
        return False
    true_pent = pents[pidx]

    for flipnum in range(3):
        p = np.copy(pent)
        if flipnum > 0:
            p = np.flip(pent, flipnum - 1)
        for rot_num in range(4):
            if np.array_equal(true_pent, p):
                return True
            p = np.rot90(p)
    return False


def add_pentomino(board, pent, coord, check_pent=False, valid_pents=None):
    """
    Adds a pentomino pent to the board. The pentomino will be placed such that
    coord[0] is the lowest row index of the pent and coord[1] is the lowest 
    column index. 
    
    check_pent will also check if the pentomino is part of the valid pentominos.
    
    将五联骨牌添加到板上。五联骨牌的放置方式是coord[0] 是 pent 的最低行索引， coord[1] 是最低的列索引。
    
    check_pent 还将检查 pentomino 是否是有效 pentomino 的一部分。
    """
    if check_pent and not is_pentomino(pent, valid_pents):
        return False
    for row in range(pent.shape[0]):
        for col in range(pent.shape[1]):
            if pent[row][col] != 0:
                if board[coord[0] + row][coord[1] + col] != 0:  # Overlap
                    return False
                else:
                    board[coord[0] + row][coord[1] + col] = pent[row][col]
    return True


def remove_pentomino(board, pent_idx):
    board[board == pent_idx + 1] = 0


def check_correctness(sol_list, board, pents):
    """
    Sol is a list of pentominos (possibly rotated) and their upper left coordinate

    Sol 是五联骨牌（可能已旋转）及其左上角坐标的列表.
    """
    # All tiles used
    # 使用的所有瓷砖
    if len(sol_list) != len(pents):
        return False
    # Construct board
    # 构造板
    sol_board = np.zeros(board.shape)
    seen_pents = [0] * len(pents)
    for pent, coord in sol_list:
        pidx = get_pent_idx(pent)
        if seen_pents[pidx] != 0:
            return False
        else:
            seen_pents[pidx] = 1
        if not add_pentomino(sol_board, pent, coord, True, pents):
            return False

    # Check same number of squares occupied
    # 检查占用的相同数量的方格
    if np.count_nonzero(board) != np.count_nonzero(sol_board):
        return False
    # Check overlap
    # 检查重叠
    if np.count_nonzero(board) != np.count_nonzero(np.multiply(board, sol_board)):
        return False

    return True


if __name__ == "__main__":
    """
    Run python Pentomino.py to check your solution. You can replace 'board' and 
    'pents' with boards of your own. You can start off easy with simple dominos.
    
    We won't gaurantee which tests your code will be run on, however if it runs
    well on the pentomino set you should be fine. 

    运行 python Pentomino.py 来检查你的解决方案。您可以替换“board”和用你自己的板子'pents'。您可以从简单的多米诺骨牌开始轻松。
    
    我们不会保证您的代码将在哪些测试上运行，但是如果它运行在 pentomino 套装上你应该没问题。
    """
    time1 = time.time()
    scale = 16
    print(f"设置的board及pents组合共{scale}组，如下所示:")
    for i in range(1, scale + 1):
        if i == 1:
            board = instances.board_6x10
            pents = instances.dominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 — 或 |， 共计{len(pents)}个")
        elif i == 2:
            board = instances.board_6x10
            pents = instances.triominos1
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 ┐ 或 ┌ 或 └ 或 ┘, 共计{len(pents)}个")
        elif i == 3:
            board = instances.board_6x10
            pents = instances.pentnominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为正宗五联牌形状, 共计{len(pents)}个")
        elif i == 4:
            board = instances.board_5x12
            pents = instances.dominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 — 或 |， 共计{len(pents)}个")
        elif i == 5:
            board = instances.board_5x12
            pents = instances.triominos1
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 ┐ 或 ┌ 或 └ 或 ┘, 共计{len(pents)}个")
        elif i == 6:
            board = instances.board_5x12
            pents = instances.pentnominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为正宗五联牌形状, 共计{len(pents)}个")
        elif i == 7:
            board = instances.board_3x20
            pents = instances.dominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 — 或 |， 共计{len(pents)}个")
        elif i == 8:
            board = instances.board_3x20
            pents = instances.triominos1
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 ┐ 或 ┌ 或 └ 或 ┘, 共计{len(pents)}个")
        elif i == 9:
            board = instances.board_3x20
            pents = instances.pentnominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为正宗五联牌形状, 共计{len(pents)}个")
        elif i == 10:
            board = instances.empty_chessboard
            pents = instances.dominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]}) ， 含有五个空格")
            print(f"pent形状均为 — 或 |， 共计{len(pents)}个")
        elif i == 11:
            board = instances.empty_chessboard
            pents = instances.triominos1
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]}) ， 含有五个空格")
            print(f"pent形状均为 ┐ 或 ┌ 或 └ 或 ┘, 共计{len(pents)}个")
        elif i == 12:
            board = instances.empty_chessboard
            pents = instances.pentnominos
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]}) ， 含有五个空格")
            print(f"pent形状均为正宗五联牌形状, 共计{len(pents)}个")
        elif i == 13:
            board = instances.board_2x6
            pents = instances.triominos2
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 ┐ 或 ┌ 或 └ 或 ┘, 共计{len(pents)}个")
        elif i == 14:
            board = instances.board_6x2
            pents = instances.triominos2
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 ┐ 或 ┌ 或 └ 或 ┘, 共计{len(pents)}个")
        elif i == 15:
            board = instances.board_2x6
            pents = instances.dominos2
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 — 或 |， 共计{len(pents)}个")
        elif i == 16:
            board = instances.board_6x2
            pents = instances.dominos2
            print(f"第{i}种组合:  棋盘大小为 ({board.shape[0]}, {board.shape[1]})")
            print(f"pent形状均为 — 或 |， 共计{len(pents)}个")
        print()

    print("输入运行的board及pents组合(1-16, 建议运行1 - 2 - 3 - 10 - 11 - 12 - 13 - 16)：")
    scale = int(input())
    if scale == 1:
        board = instances.board_6x10
        pents = instances.dominos
    elif scale == 2:
        board = instances.board_6x10
        pents = instances.triominos1
    elif scale == 3:
        board = instances.board_6x10
        pents = instances.pentnominos
    elif scale == 4:
        board = instances.board_5x12
        pents = instances.dominos
    elif scale == 5:
        board = instances.board_5x12
        pents = instances.triominos1
    elif scale == 6:
        board = instances.board_5x12
        pents = instances.pentnominos
    elif scale == 7:
        board = instances.board_3x20
        pents = instances.dominos
    elif scale == 8:
        board = instances.board_3x20
        pents = instances.triominos1
    elif scale == 9:
        board = instances.board_3x20
        pents = instances.pentnominos
    elif scale == 10:
        board = instances.empty_chessboard
        pents = instances.dominos
    elif scale == 11:
        board = instances.empty_chessboard
        pents = instances.triominos1
    elif scale == 12:
        board = instances.empty_chessboard
        pents = instances.pentnominos
    elif scale == 13:
        board = instances.board_2x6
        pents = instances.triominos2
    elif scale == 14:
        board = instances.board_6x2
        pents = instances.triominos2
    elif scale == 15:
        board = instances.board_2x6
        pents = instances.dominos2
    elif scale == 16:
        board = instances.board_6x2
        pents = instances.dominos2

    sol_list = solve(board, pents)

    time2 = time.time()
    if check_correctness(sol_list, board, pents):
        print("PASSED!")
        print("Solution:")
        num = 0
        sol_board = np.zeros(board.shape)  # 存放解的board

        for i in range(sol_board.shape[0]):
            for j in range(sol_board.shape[1]):
                if board[i][j] == 0:
                    sol_board[i][j] = -1  # 把board里的空格标记为-1
        for pent, site in sol_list:
            num += 1
            print(f"第{num}块五联骨牌")
            add_pentomino(sol_board, pent, site)
            pent = pent.tolist()
            for cell in pent:
                print(cell)
            print(f"的坐标是：({site[0] + 1}, {site[1] + 1})")
        print("最终实现的 Board 样式为：")
        print(sol_board)
    else:
        print("FAILED...")
    print("Run the result uses ：{:.4f}".format(time2 - time1), "seconds")
