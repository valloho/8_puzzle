import numpy as np
import math

class Node:
    board = np.arange(9).reshape(3, 3)
    g = 0
    h = 0
    f = 0
    parentNode = 0

# returns random start board node
def randomizeBoardNode():
    n = Node()
    randomBoard = np.arange(9)
    np.random.shuffle(randomBoard)
    n.board = np.reshape(randomBoard, (3, 3))
    return n

# inversion check
def inversionCount(node):
    count = 0
    blank = 0
    arr = node.flatten()

    for x in arr - 1: # warum -1?
        if arr[x] > arr[x + 1] and arr[x] != blank:
            count += 1
    print(count)
    return count

def solvabilityCheck(node):
    count = inversionCount(node.board)

    if count % 2 == 0:
        print("yayy, its solvable!")
    else:
        print("sadly not solvable :(")


# Return the hamming heuristic of a given node. It counts how
# many tiles are not in their designated position which indicates a minimum
# number of moves needed to solve the problem.
def hammingHeuristic(node):
    count = 0
    amount = 0

    for i in range(3):
        for j in range(3):
            if count != node.board[i][j]:
                amount += 1
            count += 1

    return amount

# Returns manhattan heuristic distance. It calculates the distance from the given
# to the designated position
def manhattanHeuristic(node):
    distance = 0

    for i in range(3):
        for j in range(3):
            row = int(node.board[i][j] / 3)
            column = node.board[i][j] % 3
            distance += abs(i - row) + abs(j - column)

    return distance
