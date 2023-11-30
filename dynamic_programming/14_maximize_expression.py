# Maximize Expression

"""
Write a function that takes in an array of integers and returns the largest possible value for the expression

array[a] - array[b] + array[c] - array[d], where a, b, c, and d are indices of the array and a < b < c < d.

if the input array has fewer than 4 elements, your function should return 0.


Sample Input
array = [3, 6, 1, -3, 2, 7]

Sample Output
4
// Choose a = 1, b = 3, c = 4, and d = 5
// => 6 - (-3) + 2 - 7 = 4

"""

# Solution 1: Brute Force
# Time: O(n^4) | Space: O(1)


def maximizeExpression(array):
    if len(array) < 4:
        return 0
    maxExpValue = float("-inf")
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                for l in range(k + 1, len(array)):
                    maxExpValue = max(maxExpValue, evaluate(array[i], array[j], array[k], array[l]))
    return maxExpValue


def evaluate(a, b, c, d):
    return a - b + c - d


# Solution 2: Dynamic Programming

# Time: O(n) | Space: O(n)

def maximizeExpression(array):
    if len(array) < 4:
        return 0
    
    maxOfA = [float("-inf") for _ in array]
    maxOfAminusB = [float("-inf") for _ in array]
    maxOfAminusBplusC = [float("-inf") for _ in array]
    maxOfAminusBplusCminusD = [float("-inf") for _ in array]

    maxOfA[0] = array[0]
    for i in range(1, len(array)):
        maxOfA[i] = max(maxOfA[i - 1], array[i])

    maxOfAminusB[1] = maxOfA[0] - array[1]
    for i in range(2, len(array)):
        maxOfAminusB[i] = max(maxOfAminusB[i - 1], maxOfA[i - 1] - array[i])

    maxOfAminusBplusC[2] = maxOfAminusB[1] + array[2]
    for i in range(3, len(array)):
        maxOfAminusBplusC[i] = max(maxOfAminusBplusC[i - 1], maxOfAminusB[i - 1] + array[i])

    maxOfAminusBplusCminusD[3] = maxOfAminusBplusC[2] - array[3]
    for i in range(4, len(array)):
        maxOfAminusBplusCminusD[i] = max(maxOfAminusBplusCminusD[i - 1], maxOfAminusBplusC[i - 1] - array[i])

    return maxOfAminusBplusCminusD[-1]