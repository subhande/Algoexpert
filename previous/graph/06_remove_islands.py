# Remove Islands

"""
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only os and
1 S. The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An island is defined as any number of 1s that are horizontally or vertically adjacent (but not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1 s isn't an island if any of those 1 s are in the first row, last row, first column, or last column of the input matrix.

Note that an island can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.

You can think of islands as patches of black that don't touch the border of the two-toned image.
Write a function that returns a modified version of the input matrix, where all of the islands are removed. You remove an island by replacing it with o s.
Naturally, you're allowed to mutate the input matrix.

Sample Input

Sample Input
matrix =
[
[1, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 1],
[O, 0, 1, 0, 1, 0],
[1, 1, 0, 0, 1, 0],
[1, 0, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 1],
]
Sample Output
[
[1, 0, 0, 0, 0, 0]
[O, 0, 0, 1, 1, 1],
[O, 0, 0, 0, 1, 0],
[1, 1, 0, 0, 1, 0],
[1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 1]],

// The islands can be clearly seen here:


"""

def isIsland(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return matrix[i][j] == 1

def islandPresentInNeighbour(matrix, i, j):
    left = isIsland(matrix, i-1, j)
    right = isIsland(matrix, i+1, j)
    top = isIsland(matrix, i, j-1)
    bottom = isIsland(matrix, i, j+1)
    return left, right, top, bottom

def isBorder(i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return i == 0 or i == n-1 or j == 0 or j == m-1

# Time: O(wh) | Space: O(wh) - where w is the width and h is the height of the input matrix
def removeIslands(matrix):
    islands = []
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            currentIsland = []
            currentIslandContainsBorder = False
            if visited[i][j]:
                continue
            # visited[i][j] = True
            # if isBorder(i, j, n, m) or matrix[i][j] == 0:
            #     continue 
            nodeToExplore = [[i, j]]
            while nodeToExplore:
                i, j = nodeToExplore.pop()
                if visited[i][j]:
                    continue
                visited[i][j] = True
                __isborder = isBorder(i, j, n, m)
                currentIslandContainsBorder = currentIslandContainsBorder or __isborder
                __island = isIsland(matrix, i, j)
                if not __island:
                    continue
                currentIsland.append([i, j])
                left, right, top, bottom = islandPresentInNeighbour(matrix, i, j)
                if left:
                    nodeToExplore.append([i-1, j])
                if right:
                    nodeToExplore.append([i+1, j])
                if top:
                    nodeToExplore.append([i, j-1])
                if bottom:
                    nodeToExplore.append([i, j+1])
            if currentIsland and currentIslandContainsBorder is False:
                islands.append(currentIsland)
    for island in islands:
        for i, j in island:
            matrix[i][j] = 0
    return matrix


# Algoexpert solution 1: [O(wh) time | O(wh) space] [Optimal]

def removeIslands(matrix):
    onesConnectedToBorder = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[0]) - 1
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue
            findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if onesConnectedToBorder[row][col]:
                continue
            matrix[row][col] = 0
    return matrix

def findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder):
    stack = [[row, col]]

    while len(stack) > 0:
        curreentPosition = stack.pop()
        currentRow, currentCol = curreentPosition
        alreadyVisited = onesConnectedToBorder[currentRow][currentCol]
        if alreadyVisited:
            continue
        onesConnectedToBorder[currentRow][currentCol] = True
        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] != 1:
                continue
            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []
    if row - 1 >= 0: # UP
        neighbors.append([row - 1, col])
    if row + 1 < len(matrix): # DOWN
        neighbors.append([row + 1, col])
    if col - 1 >= 0: # LEFT
        neighbors.append([row, col - 1])
    if col + 1 < len(matrix[0]): # RIGHT
        neighbors.append([row, col + 1])
    return neighbors

# Algoexpert solution 1: [O(wh) time | O(wh) space] [Optimal]

def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            isRowBorder = row == 0 or row == len(matrix) - 1
            isColBorder = col == 0 or col == len(matrix[0]) - 1
            isBorder = isRowBorder or isColBorder
            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue
            changeOnesConnectedToBorderToTwos(matrix, row, col)


    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
            elif matrix[row][col] == 2:
                matrix[row][col] = 1



def changeOnesConnectedToBorderToTwos(matrix, row, col):
    stack = [[row, col]]
    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition
        matrix[currentRow][currentCol] = 2
        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] != 1:
                continue
            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []
    if row - 1 >= 0: # UP
        neighbors.append([row - 1, col])
    if row + 1 < len(matrix): # DOWN
        neighbors.append([row + 1, col])
    if col - 1 >= 0: # LEFT
        neighbors.append([row, col - 1])
    if col + 1 < len(matrix[0]): # RIGHT
        neighbors.append([row, col + 1])
    return neighbors




if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    print(removeIslands(matrix))