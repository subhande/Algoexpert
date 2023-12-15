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
       /    /   \
     5     12     94
   /       /      /
  2       11     81


"""

# Solution 1


# Time: O(n^2) | Space: O(n^2)
def getSmaller(array, ele):
    return [item for item in array if item < ele]


def getBiggerOrEqual(array, ele):
    return [item for item in array if item >= ele]


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False

    if len(arrayOne) == 1 and len(arrayTwo) == 1 and arrayOne[0] == arrayTwo[0]:
        return True

    leftOne = getSmaller(arrayOne[1:], arrayOne[0])
    rightOne = getBiggerOrEqual(arrayOne[1:], arrayOne[0])

    leftTwo = getSmaller(arrayTwo[1:], arrayTwo[0])
    rightTwo = getBiggerOrEqual(arrayTwo[1:], arrayTwo[0])

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


# Solution 2

# Time: O(n^2) | Space: O(d)


def sameBsts(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)

    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

    currentValue = arrayOne[rootIdxOne]

    leftAreSame = areSameBsts(
        arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue
    )
    rightAreSame = areSameBsts(
        arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal
    )

    return leftAreSame and rightAreSame


def getIdxOfFirstSmaller(array, startingIdx, minVal):
    for i in range(startingIdx+1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal:
            return i
    return -1


def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    for i in range(startingIdx+1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1
