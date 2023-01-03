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

    for x in arr -1:
        if arr[x] > arr[x + 1] and arr[x] != blank:
            count += 1
    print(count)
    return count