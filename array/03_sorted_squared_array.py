# Sorted Squared Array
# Write a function that takes in a non-empty array of integers that are sorted
# in ascending order and returns a new array of the same length with the squares
# of the original integers also sorted in ascending order.
# Sample Input
# array = [1, 2, 3, 5, 6, 8, 9]
# Sample Output
# [1, 4, 9, 25, 36, 64, 81]

# array = [-3, 1, 2, 5, 6, 8, 9]
# Sample Output
# [1, 4, 9, 25, 36, 64, 81]

# Time Complexity: O(nlogn) | Space Complexity: O(n)
def sortedSquaredArray(array):
    return sorted([i**2 for i in array])

# Time Complexity: O(n) | Space Complexity: O(n)
def sortedSquaredArray(array):
    sortedSquares = [0] * len(array)
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue  = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue ** 2
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue ** 2
            largerValueIdx -= 1
    return sortedSquares
