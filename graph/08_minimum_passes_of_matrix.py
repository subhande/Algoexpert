# Minimum Passes Of Matrix

"""
Write a function that takes in an integer matrix of potentially unequal height and width and returns the minimum number of passes required to convert all negative integers in the matrix to positive integers.
A negative integer in the matrix can only be converted to a positive integer if one or more of its adjacent elements is positive. An adjacent element is an element that is to the left, to the right, above, or below the current element in the matrix. Converting a negative to a positive simply involves multiplying it by |
-1
Note that the 0 value is neither positive nor negative, meaning that a © can't convert an adjacent negative to a positive.

A single pass through the matrix involves converting all the negative integers that can be converted at a particular point in time. For example, consider the following input matrix:

[
    [0, -2, -1],
    [-5, 2, 0],
    [-6, -2, 0],
]

After a first pass, only 3 values can be converted to positive:

[
    [0, -2, -1],
    [5, 2, 0],
    [-6, 2, 0],
]

After a second pass, all the remaining negative values can be converted to positive:

[
    [0, 2, 1],
    [5, 2, 0],
    [6, 2, 0],
]

Note that the input matrix will always contain at least one element. If the negative integers in the input matrix can't be all converted to positives, regardless of how many passes are run, your function should return -1.

Sample Input

matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

Sample Output
3



"""
from copy import deepcopy

# Brute Force

def isPositive(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return matrix[i][j] > 0


def isNeighbourPositive(matrix, i, j):
    left = isPositive(matrix, i - 1, j)
    right = isPositive(matrix, i + 1, j)
    top = isPositive(matrix, i, j - 1)
    bottom = isPositive(matrix, i, j + 1)
    return left or right or top or bottom

# Time: O(whp) | Space: O(wh) - where w is the width of the matrix, h is the height of the matrix and p is the number of itaration over the matrix
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = -1
    new_matrix = deepcopy(matrix)
    while True:
        n = len(matrix)
        m = len(matrix[0])
        no_change = True
        is_negative_present = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] < 0:
                    is_negative_present = True
                if matrix[i][j] < 0 and isNeighbourPositive(matrix, i, j):
                    new_matrix[i][j] *= -1
                    no_change = False
        matrix = deepcopy(new_matrix)
        if is_negative_present is False and passes == -1:
            return 0
        if is_negative_present and no_change:
            return -1
        if no_change:
            break

        passes += 1
    return passes if passes == -1 else passes + 1

# Algoexpert Solution 1: Optimal Solution
# Time: O(wh) | Space: O(wh) - where w is the width of the matrix, h is the height of the matrix
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = convertNegative(matrix)
    return passes if not containsNegative(matrix) else -1

def convertNegative(matrix):
    nextPassQueue = getAllPositivePositions(matrix)

    passes = -1

    while len(nextPassQueue) > 0:
        currentPassQueue = nextPassQueue
        nextPassQueue = []
        while len(currentPassQueue) > 0:
            currentRow, currentCol = currentPassQueue.pop(0)
            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    nextPassQueue.append([row, col])
        passes += 1

    return passes

def getAllPositivePositions(matrix):
    positivePositions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positivePositions.append([row, col])
    return positivePositions

def getAdjacentPositions(row, col, matrix):
    adjacentPositions = []
    if row > 0:
        adjacentPositions.append([row - 1, col])
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])
    if col > 0:
        adjacentPositions.append([row, col - 1])
    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])
    return adjacentPositions

def containsNegative(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value < 0:
                return True
    return False

# Algoexpert Solution 1: Optimal Solution

def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = convertNegative(matrix)
    return passes if not containsNegative(matrix) else -1

def convertNegative(matrix):
    queue = getAllPositivePositions(matrix)

    passes = -1

    while len(queue) > 0:
        currentSize = len(queue)
        
        while currentSize > 0:
            currentRow, currentCol = queue.pop(0)
            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    queue.append([row, col])
            currentSize -= 1
        passes += 1
    return passes



if __name__ == "__main__":
    matrix = [
        [1, 0, 0, -2, -3],
        [-4, -5, -6, -2, -1],
        [0, 0, 0, 0, -1],
        [-1, 0, 3, 0, 3],
    ]
    print(minimumPassesOfMatrix(matrix))
