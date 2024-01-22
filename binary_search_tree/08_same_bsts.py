
# Same BSTs

"""
An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array, from left to right, into the BST.

Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST. Note that you're not allowed to construct any BSTs in your code.

A BST is a Binary Tree that consists only of BST nodes. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.


Sample Input
arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]


Sample Output
true // both arrays represent the BST below
        10
       /   \
      8     15
     /       \
    5        94
   /        /
  2        81
           /
         12
        /
       11

"""

# Solution 1: Recursion

def getSmallerAndBiggerOrEqual(array):
    smaller = []
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
        else:
            biggerOrEqual.append(array[i])
    return smaller, biggerOrEqual


# Time: O(n^2) | Space: O(n^2)
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
    smallerOne, biggerOrEqualOne = getSmallerAndBiggerOrEqual(arrayOne)
    smallerTwo, biggerOrEqualTwo = getSmallerAndBiggerOrEqual(arrayTwo)

    return sameBsts(smallerOne, smallerTwo) and sameBsts(biggerOrEqualOne, biggerOrEqualTwo)


# Solution 2: Optimal Solution

# Time: O(n^2) | Space: O(d)
def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxval):

    # Check if the root nodes are out of bounds
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo
    
    # Check if the root nodes are different
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False
    

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxval)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxval)

    currentValue = arrayOne[rootIdxOne]
    leftAreSame = areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame = areSameBsts(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxval)

    return leftAreSame and rightAreSame


def getIdxOfFirstSmaller(array, startingIdx, minVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal:
            return i
    return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1
    

    

    



