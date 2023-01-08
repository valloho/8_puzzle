import numpy as np


# generates a shuffled start node
def generateStartNode():
    node = Node(0, 0, 0, None, 0)
    board = np.arange(9)  # generates an array with numbers 0-8
    np.random.shuffle(board)  # shuffles the array entries randomly
    node.board = np.reshape(board, (3, 3))  # reshapes the array into 3x3 matrix
    print(node.board)

    if node.isSolvable():
        return node
    else:
        return generateStartNode()


# generates a goal node with correct order of entries 0-1
def generateGoalNode():
    node = Node(0, 0, 0, parent=None, board=0)
    node.board = np.arange(9).reshape(3, 3)
    print(node.board)
    return node


class Node:
    g = 0  #
    h = 0
    f = 0
    parent = None
    board = np.empty(9, dtype=int)

    # constructor of Node class
    def __init__(self, g, h, f, parent, board):
        self.g = g
        self.h = h
        self.f = f
        self.parent = parent
        self.board = board

    # iterates array and counts inversions
    def inversionCount(self):
        count = 0
        arr = self.board.flatten()  # flattens multidimensional array into one dimension for simpler iteration

        for i in range(8):
            if arr[i] > arr[i + 1] and arr[i] != 0:
                count += 1

        return count

    # checks if puzzle is solvable
    def isSolvable(self):
        count = self.inversionCount()

        if count % 2 == 0:  # puzzle is solvable if number of inversions is even
            return 1
        else:
            return 0

    # calculates the hamming heuristic of a given node. It compares the start and goal node and
    # counts how many tiles are misplaced which indicates a minimum number of moves needed
    # to solve the problem.
    def calcHamming(self, goal):
        h_value = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != goal.board[i][j]:
                    h_value += 1

        self.h = h_value
        print(h_value)
        return h_value

    # Returns manhattan heuristic distance. It calculates the distance from the given
    # to the designated position.
    def calcManhattan(self, goal):
        h_value = 0

        for i in range(3):
            for j in range(3):
                start_row = int(self.board[i][j] / 3)
                start_col = self.board[i][j] % 3
                goal_row = int(goal.board[i][j] / 3)
                goal_col = goal.board[i][j] % 3

                h_value += abs(start_row - goal_row) + abs(start_col - goal_col)

        self.h = h_value
        return h_value


if __name__ == "__main__":
    start = generateStartNode()
    goal = generateGoalNode()
    start.calcHamming(goal)
