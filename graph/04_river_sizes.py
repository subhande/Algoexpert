# River Sizes

"""
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.

Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.

Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

Sample Input

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]   

Sample Output

[1, 2, 2, 2, 5] // The numbers could be ordered differently.

The rivers can be clearly seen here:

[
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

"""

# My Code

def isRiver(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return matrix[i][j] == 1

def riverPresentInNeighbour(matrix, i, j):
    left = isRiver(matrix, i-1, j)
    right = isRiver(matrix, i+1, j)
    top = isRiver(matrix, i, j-1)
    bottom = isRiver(matrix, i, j+1)
    return left, right, top, bottom

# Time: O(wh)  | Space: O(wh)
def riverSizes(matrix):
    n =  len(matrix)
    m = len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    riverSizes = []
    for i in range(n):
        for j in range(m):
            currentRiverSize = 0
            nodesToExplore = [[i, j]]
            while len(nodesToExplore):
                currentNode = nodesToExplore.pop()
                i = currentNode[0]
                j = currentNode[1]
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if not isRiver(matrix, i, j):
                    continue
                currentRiverSize += 1
                left, right, top, bottom = riverPresentInNeighbour(matrix, i, j)
                if left:
                    nodesToExplore.append([i-1, j])
                if right:
                    nodesToExplore.append([i+1, j])
                if top:
                    nodesToExplore.append([i, j-1])
                if bottom:
                    nodesToExplore.append([i, j+1])
            if currentRiverSize > 0:
                riverSizes.append(currentRiverSize)
    return riverSizes
                

# Algoexpert

# Time: O(wh)  | Space: O(wh)
def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbours(i, j, matrix, visited):
    unvisitedNeighbours = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbours.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbours.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbours.append([i, j + 1])
    return unvisitedNeighbours