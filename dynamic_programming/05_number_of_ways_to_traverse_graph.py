# Number of ways to traverse a graph

"""
You're given two positive integers representing the width and height of a grid-shaped, rectangular graph. Write a function that returns the number of ways to reach the bottom right corner of the graph when starting at the top left corner. Each move you take must either go down or right. In other words, you can never move up or left in the graph.

For example, given the graph illustrated below, with width = 2 and height = 3, there are three ways to reach the bottom right corner when starting at the top left corner:

 __ __
|__|__|
|__|__|
|__|__|



1. Down, Down, Right
2. Right, Down, Down
3. Down, Right, Down

Note: you may assume that width * height >= 2. In other words, the graph will never be a 1x1 grid.

Sample Input
width = 4
height = 3

Sample Output
10

"""

# Solution 1: Recusion
# Time: O(2^(n+m)) | Space: O(n+m)
def numberOfWaysToTraverseGraph(width, height):
    if width == 1 and height == 1:
        return 1
    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height-1)


# Solution 2: Dynamic Programming
# Time: O(nm) | Space: O(nm)
def numberOfWaysToTraverseGraph(width, height):
    numberOfWays = [[0 for _ in range(width+1)] for _ in range(height+1)]

    for heightIdx in range(1, height+1):
        for widthIdx in range(1, width + 1):
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                waysLeft = numberOfWays[heightIdx][widthIdx-1]
                waysUp = numberOfWays[heightIdx-1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp
    return numberOfWays[height][width]


# Solution 3: Optimised Math Formula
# Time: O(n+m) | Space: O(1)
def numberOfWaysToTraverseGraph(width, height):
    xDistanceToCorner = width - 1
    yDistanceToCorner = height - 1

    numerator = factorial(xDistanceToCorner + yDistanceToCorner) 
    denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)
    return numerator // denominator


def factorial(num):
    result = 1
    for n in range(2, num+1):
        result *= n
