from time import sleep
from math import inf
from random import randint, choice


class ultimateTicTacToe:
    def __init__(self):
        """
        Initialization of the game.
        """
        self.board = [['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_', '_']]

        self.maxPlayer = 'X'
        self.minPlayer = 'O'
        self.maxDepth = 3
        # The start indexes of each local board
        self.globalIdx = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        # Start local board index for reflex agent playing
        self.startBoardIdx = 4
        # self.startBoardIdx=randint(0,8)
        self.curt_board_idx = 0

        # utility value for reflex offensive and reflex defensive agents
        self.winnerMaxUtility = 10000
        self.twoInARowMaxUtility = 500
        self.preventThreeInARowMaxUtility = 100
        self.cornerMaxUtility = 30

        self.winnerMinUtility = -10000
        self.twoInARowMinUtility = -100
        self.preventThreeInARowMinUtility = -500
        self.cornerMinUtility = -30

        self.expandedNodes = 0
        self.currPlayer = True
        self.curt_evaluation = self.evaluatePredifined

        self.moves = list((x, y) for x in range(3) for y in range(3))

    def printGameBoard(self):
        """
        This function prints the current game board.
        """
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.board[:3]]) + '\n')
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.board[3:6]]) + '\n')
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in self.board[6:9]]) + '\n')

    def two_in_row(self, isMax):
        """
        :return: the number of unblocked two-in-row for the player
                 and the number of blocked two-in-row for the opponent
        """
        mine, yours = 'O', 'X'
        mine_unblocked, yours_blocked = 0, 0

        if isMax:
            mine, yours = yours, mine

        for x, y in self.globalIdx:
            diagonals, rows, columns = list(), list(), list()

            diagonals.append([self.board[x][y], self.board[x + 1][y + 1], self.board[x + 2][y + 2]])
            diagonals.append([self.board[x][y + 2], self.board[x + 1][y + 1], self.board[x + 2][y]])

            for row in range(3):
                rows.append([self.board[x + row][y], self.board[x + row][y + 1], self.board[x + row][y + 2]])

            for column in range(3):
                columns.append(
                    [self.board[x][y + column], self.board[x + 1][y + column], self.board[x + 2][y + column]])

            for line in diagonals + rows + columns:
                if line.count(mine) == 2 and line.count(yours) == 0:
                    mine_unblocked += 1
                if line.count(yours) == 2 and line.count(mine) == 1:
                    yours_blocked += 1

        return mine_unblocked, yours_blocked

    def corner_taken(self, isMax):
        if isMax:
            mine = 'X'
        else:
            mine = 'O'

        num_corner_taken = 0

        for x, y in self.globalIdx:
            if self.board[x][y] == mine:
                num_corner_taken += 1

            if self.board[x + 2][y] == mine:
                num_corner_taken += 1

            if self.board[x][y + 2] == mine:
                num_corner_taken += 1

            if self.board[x + 2][y + 2] == mine:
                num_corner_taken += 1

        return num_corner_taken

    def center_taken(self, isMax):
        if isMax:
            mine = 'X'
        else:
            mine = 'O'

        num_center_taken = 0

        for x, y in self.globalIdx:
            if self.board[x + 1][y + 1] == mine:
                num_center_taken += 1
        return num_center_taken

    def side_taken(self, isMax):
        if isMax:
            mine = 'X'
        else:
            mine = 'O'

        num_side_taken = 0

        for x, y in self.globalIdx:
            if self.board[x][y + 1] == mine:
                num_side_taken += 1
            if self.board[x + 1][y] == mine:
                num_side_taken += 1
            if self.board[x + 2][y + 1] == mine:
                num_side_taken += 1
            if self.board[x + 1][y + 2] == mine:
                num_side_taken += 1
        return num_side_taken

    def evaluatePredifined(self, isMax):
        """
        This function implements the evaluation function for ultimate tic tac toe for predifined agent.
        input args:
        isMax(bool): boolean variable indicates whether it's maxPlayer or minPlayer.
                     True for maxPlayer, False for minPlayer
        output:
        score(float): estimated utility score for maxPlayer or minPlayer
        """
        # YOUR CODE HERE
        if isMax:
            if self.checkWinner() == 1:
                return self.winnerMaxUtility

            mine_unblocked, yours_blocked = self.two_in_row(isMax)
            if mine_unblocked or yours_blocked:
                return mine_unblocked * self.twoInARowMaxUtility + yours_blocked * self.preventThreeInARowMaxUtility

            return self.corner_taken(isMax) * self.cornerMaxUtility
        else:
            if self.checkWinner() == -1:
                return self.winnerMinUtility

            mine_unblocked, yours_blocked = self.two_in_row(isMax)
            if mine_unblocked or yours_blocked:
                return mine_unblocked * self.twoInARowMinUtility + yours_blocked * self.preventThreeInARowMinUtility

            return self.corner_taken(isMax) * self.cornerMinUtility

    def check_will_lose(self):
        mine, yours = 'O', 'X'
        x, y = self.globalIdx[self.curt_board_idx]

        diagonals, rows, columns = list(), list(), list()

        diagonals.append([self.board[x][y], self.board[x + 1][y + 1], self.board[x + 2][y + 2]])
        diagonals.append([self.board[x][y + 2], self.board[x + 1][y + 1], self.board[x + 2][y]])

        for row in range(3):
            rows.append([self.board[x + row][y], self.board[x + row][y + 1], self.board[x + row][y + 2]])

        for column in range(3):
            columns.append([self.board[x][y + column], self.board[x + 1][y + column], self.board[x + 2][y + column]])

        for line in diagonals + rows + columns:
            if line.count(yours) == 2 and line.count(mine) == 0:
                return True

        return False

    def evaluateDesigned(self, isMax):
        """
        This function implements the evaluation function for ultimate tic tac toe for your own agent.
        input args:
        isMax(bool): boolean variable indicates whether it's maxPlayer or minPlayer.
                     True for maxPlayer, False for minPlayer
        output:
        score(float): estimated utility score for maxPlayer or minPlayer
        """
        # YOUR CODE HERE
        utility = 0
        if not isMax:
            if self.checkWinner() == 1:
                utility = float('inf')
                return utility

            if self.checkWinner() == -1:
                utility = -float('inf')
                return utility

            # two-in-a-row
            mine_unblocked, yours_blocked = self.two_in_row(isMax)
            if mine_unblocked or yours_blocked:
                utility += mine_unblocked * 200 + yours_blocked * 100

            yours_unblocked, mine_blocked = self.two_in_row(not isMax)
            if mine_unblocked or yours_blocked:
                utility += yours_unblocked * (-200) + mine_blocked * (-100)

            # corner
            utility += self.corner_taken(isMax) * 30 + self.corner_taken(not isMax) * (-30)

            # center
            utility += self.center_taken(isMax) * 60 + self.center_taken(not isMax) * (-60)

            # side
            utility += self.side_taken(isMax) * 10 + self.side_taken(not isMax) * (-10)

            return utility

        else:
            if self.checkWinner() == -1:
                utility = float('inf')
                return utility

            if self.checkWinner() == 1:
                utility = -float('inf')
                return utility

            # two-in-a-row
            mine_unblocked, yours_blocked = self.two_in_row(not isMax)
            if mine_unblocked or yours_blocked:
                utility += mine_unblocked * 200 + yours_blocked * 100

            yours_unblocked, mine_blocked = self.two_in_row(isMax)
            if mine_unblocked or yours_blocked:
                utility += yours_unblocked * (-200) + mine_blocked * (-100)

            # corner
            utility += self.corner_taken(not isMax) * 30 + self.corner_taken(isMax) * (-30)

            # center
            utility += self.center_taken(not isMax) * 60 + self.center_taken(not isMax) * (-60)

            # side
            utility += self.side_taken(not isMax) * 10 + self.side_taken(isMax) * (-10)

            return utility

    def checkMovesLeft(self):
        """
        This function checks whether any legal move remains on the board.
        output:
        movesLeft(bool): boolean variable indicates whether any legal move remains
                        on the board.
        """
        # YOUR CODE HERE
        return any(self.board[x][y] == '_' for x in range(len(self.board)) for y in range(len(self.board[0])))

    def checkWinner(self):
        # Return termimnal node status for maximizer player 1-win,0-tie,-1-lose
        """
        This function checks whether there is a winner on the board.
        output:
        winner(int): Return 0 if there is no winner.
                     Return 1 if maxPlayer is the winner.
                     Return -1 if miniPlayer is the winner.
        """
        # YOUR CODE HERE
        for x, y in self.globalIdx:
            if self.board[x][y] == self.board[x + 1][y + 1] == self.board[x + 2][y + 2] \
                    or self.board[x][y + 2] == self.board[x + 1][y + 1] == self.board[x + 2][y]:
                if self.board[x + 1][y + 1] == 'X':
                    return 1
                elif self.board[x + 1][y + 1] == 'O':
                    return -1

            for row in range(3):
                if self.board[x + row][y] == self.board[x + row][y + 1] == self.board[x + row][y + 2]:
                    if self.board[x + row][y] == 'X':
                        return 1
                    elif self.board[x + row][y] == 'O':
                        return -1

            for column in range(3):
                if self.board[x][y + column] == self.board[x + 1][y + column] == self.board[x + 2][y + column]:
                    if self.board[x][y + column] == 'X':
                        return 1
                    elif self.board[x][y + column] == 'O':
                        return -1

        return 0

    def alphabeta(self, depth, currBoardIdx, alpha, beta, isMax):
        """
        This function implements alpha-beta algorithm for ultimate tic-tac-toe game.
        input args:
        depth(int): current depth level
        currBoardIdx(int): current local board index
        alpha(float): alpha value
        beta(float): beta value
        isMax(bool):boolean variable indicates whether it's maxPlayer or minPlayer.
                     True for maxPlayer, False for minPlayer
        output:
        bestValue(float):the bestValue that current player may have
        """
        # YOUR CODE HERE

        if depth == self.maxDepth:
            return self.curt_evaluation(isMax)

        x, y = self.globalIdx[currBoardIdx]

        if (isMax and depth % 2 == 1) or (not isMax and depth % 2 == 0):
            # the situation where we look for the minimum value
            curt_move = 'O'
            curt_best = float('inf')
        else:
            curt_move = 'X'
            curt_best = -float('inf')

        for xd, yd in self.moves:
            if self.board[x + xd][y + yd] != '_':
                continue

            self.board[x + xd][y + yd] = curt_move
            self.expandedNodes += 1
            nxt_local_board = xd * 3 + yd
            new_best = self.alphabeta(depth + 1, nxt_local_board, alpha, beta, isMax)
            self.board[x + xd][y + yd] = '_'

            if (isMax and depth % 2 == 1) or (not isMax and depth % 2 == 0):
                curt_best = min(curt_best, new_best)
                if curt_best <= alpha:
                    return curt_best
                beta = min(beta, curt_best)

            else:
                curt_best = max(curt_best, new_best)
                if curt_best >= beta:
                    return curt_best
                alpha = max(alpha, curt_best)

        return curt_best

    def minimax(self, depth, currBoardIdx, isMax):
        """
        This function implements minimax algorithm for ultimate tic-tac-toe game.
        input args:
        depth(int): current depth level
        currBoardIdx(int): current local board index
        alpha(float): alpha value
        beta(float): beta value
        isMax(bool):boolean variable indicates whether it's maxPlayer or minPlayer.
                     True for maxPlayer, False for minPlayer
        output:
        bestValue(float):the bestValue that current player may have
        """
        # YOUR CODE HERE

        if depth == self.maxDepth:
            return self.curt_evaluation(isMax)

        x, y = self.globalIdx[currBoardIdx]

        if (isMax and depth % 2 == 1) or (not isMax and depth % 2 == 0):
            # the situation where we look for the minimum value
            curt_move = 'O'
            curt_best = float('inf')
        else:
            curt_move = 'X'
            curt_best = -float('inf')

        for xd, yd in self.moves:
            if self.board[x + xd][y + yd] != '_':
                continue

            self.board[x + xd][y + yd] = curt_move
            self.expandedNodes += 1
            nxt_local_board = xd * 3 + yd
            new_best = self.minimax(depth + 1, nxt_local_board, isMax)
            self.board[x + xd][y + yd] = '_'

            if (isMax and depth % 2 == 1) or (not isMax and depth % 2 == 0):
                curt_best = min(curt_best, new_best)
            else:
                curt_best = max(curt_best, new_best)

        return curt_best

    def playGamePredifinedAgent(self, maxFirst, isMinimaxOffensive, isMinimaxDefensive):
        """
        This function implements the processes of the game of predifined offensive agent vs defensive agent.
        input args:
        maxFirst(bool): boolean variable indicates whether maxPlayer or minPlayer plays first.
                        True for maxPlayer plays first, and False for minPlayer plays first.
        isMinimaxOffensive(bool):boolean variable indicates whether it's using minimax or alpha-beta pruning algorithm for offensive agent.
                        True is minimax and False is alpha-beta.
        isMinimaxOffensive(bool):boolean variable indicates whether it's using minimax or alpha-beta pruning algorithm for defensive agent.
                        True is minimax and False is alpha-beta.
        output:
        bestMove(list of tuple): list of bestMove coordinates at each step
        bestValue(list of float): list of bestValue at each move
        expandedNodes(list of int): list of expanded nodes at each move
        gameBoards(list of 2d lists): list of game board positions at each move
        winner(int): 1 for maxPlayer is the winner, -1 for minPlayer is the winner, and 0 for tie.
        """
        # YOUR CODE HERE
        bestMove = []
        bestValue = []
        winner = 0

        isMax = True
        if not maxFirst:
            isMax = False

        if isMinimaxOffensive:
            offensive_algo = self.minimax
        else:
            offensive_algo = self.alphabeta

        if isMinimaxDefensive:
            defensive_algo = self.minimax
        else:
            defensive_algo = self.alphabeta

        curt_local_board = self.startBoardIdx

        while self.checkMovesLeft():
            winner = self.checkWinner()
            if winner:
                break

            if isMax:
                curt_move = 'X'
                curt_algo = offensive_algo
                curt_best = -float('inf')
            else:
                curt_move = 'O'
                curt_algo = defensive_algo
                curt_best = float('inf')

            x, y = self.globalIdx[curt_local_board]
            best_x, best_y = self.globalIdx[curt_local_board]

            for xd, yd in self.moves:
                if self.board[x + xd][y + yd] != '_':
                    continue

                self.board[x + xd][y + yd] = curt_move
                self.expandedNodes += 1
                if curt_algo == self.minimax:
                    new_best = curt_algo(1, xd * 3 + yd, isMax)
                else:
                    new_best = curt_algo(1, xd * 3 + yd, -float('inf'), float('inf'), isMax)

                self.board[x + xd][y + yd] = '_'

                if isMax:
                    if new_best > curt_best:
                        curt_best = new_best
                        best_x, best_y = x + xd, y + yd
                else:
                    if new_best < curt_best:
                        curt_best = new_best
                        best_x, best_y = x + xd, y + yd

            self.board[best_x][best_y] = curt_move
            self.printGameBoard()

            bestMove.append((best_x, best_y))
            bestValue.append(curt_best)

            isMax = not isMax
            curt_local_board = (best_x - x) * 3 + (best_y - y)

        return self.board, bestMove, self.expandedNodes, bestValue, winner

    def playGameYourAgent(self):
        """
        This function implements the processes of the game of your own agent vs predifined offensive agent.
        input args:
        output:
        bestMove(list of tuple): list of bestMove coordinates at each step
        gameBoards(list of 2d lists): list of game board positions at each move
        winner(int): 1 for maxPlayer is the winner, -1 for minPlayer is the winner, and 0 for tie.
        """
        # YOUR CODE HERE
        bestMove = []
        winner = 0

        offensive_algo = self.alphabeta
        defensive_algo = self.alphabeta

        curt_board_idx = randint(0, 8)
        isMax = choice([True, False])

        if not isMax:
            self.curt_evaluation = self.evaluateDesigned

        while self.checkMovesLeft():
            winner = self.checkWinner()
            if winner:
                break

            if isMax:
                curt_move = 'X'
                curt_algo = offensive_algo
                curt_best = -float('inf')
            else:
                curt_move = 'O'
                curt_algo = defensive_algo
                curt_best = float('inf')

            x, y = self.globalIdx[curt_board_idx]
            best_x, best_y = self.globalIdx[curt_board_idx]

            for xd, yd in self.moves:
                if self.board[x + xd][y + yd] != '_':
                    continue

                self.board[x + xd][y + yd] = curt_move
                self.expandedNodes += 1
                if curt_algo == self.minimax:
                    new_best = curt_algo(1, xd * 3 + yd, isMax)
                else:
                    new_best = curt_algo(1, xd * 3 + yd, -float('inf'), float('inf'), isMax)

                self.board[x + xd][y + yd] = '_'

                if isMax:
                    if new_best > curt_best:
                        curt_best = new_best
                        best_x, best_y = x + xd, y + yd
                else:
                    if new_best < curt_best:
                        curt_best = new_best
                        best_x, best_y = x + xd, y + yd

            self.board[best_x][best_y] = curt_move

            bestMove.append((best_x, best_y))

            isMax = not isMax
            curt_board_idx = (best_x - x) * 3 + (best_y - y)

            if self.curt_evaluation == self.evaluatePredifined:
                self.curt_evaluation = self.evaluateDesigned
            else:
                self.curt_evaluation = self.evaluatePredifined

        return self.board, bestMove, winner

    def playGameHuman(self):
        """
        This function implements the processes of the game of your own agent vs a human.
        output:
        bestMove(list of tuple): list of bestMove coordinates at each step
        gameBoards(list of 2d lists): list of game board positions at each move
        winner(int): 1 for maxPlayer is the winner, -1 for minPlayer is the winner, and 0 for tie.
        """
        # YOUR CODE HERE
        bestMove = []
        gameBoards = []
        winner = 0
        return gameBoards, bestMove, winner


if __name__ == "__main__":
    uttt = ultimateTicTacToe()

    uttt.board = [['X', '_', '_', '_', '_', '_', '_', '_', '_'],
                  ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
                  ['O', '_', 'O', '_', '_', '_', '_', '_', '_'],
                  ['_', '_', '_', 'O', 'X', 'O', '_', '_', '_'],
                  ['_', '_', '_', 'O', '_', 'X', '_', '_', '_'],
                  ['_', '_', '_', 'X', 'O', 'O', '_', '_', '_'],
                  ['O', '_', '_', '_', '_', '_', '_', '_', '_'],
                  ['_', '_', '_', '_', '_', '_', '_', 'O', '_'],
                  ['_', '_', '_', '_', '_', 'O', 'O', 'X', 'X']]
    uttt.printGameBoard()

    # print(uttt.checkWinner())
    print(uttt.checkMovesLeft())
    # print(uttt.evaluatePredifined(True))
    # print(uttt.evaluatePredifined(False))
    # print(uttt.playGamePredifinedAgent(True, True, True))
    # board, steps, winner = uttt.playGameYourAgent()
    # print(steps)
    #
    gameBoards, bestMove, expandedNodes, bestValue, winner=uttt.playGamePredifinedAgent(True, True, True)
    uttt.printGameBoard()
    if winner == 1:
        print("The winner is maxPlayer!!!")
    elif winner == -1:
        print("The winner is minPlayer!!!")
    else:
        print("Tie. No winner:(")

    # win = 0
    # print("running")
    # for i in range(100):
    #     uttt = ultimateTicTacToe()
    #     if uttt.playGameYourAgent()[2] == -1:
    #         win += 1
    #
    # print("In 100 games, your agent winning times:")
    # print(win)