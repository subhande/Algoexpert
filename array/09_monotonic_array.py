# Monotonic Array
"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Sample Output
true
"""
# Time: O(n) | Space: O(1)
def isMonotonic(array):
    if len(array) in [0, 1]:
        return True
    isNonDecresing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if isNonDecresing and array[i] < array[i-1]:
            isNonDecresing = False
        if isNonIncreasing and array[i] > array[i-1]:
            isNonIncreasing = False
        if isNonDecresing is False and isNonIncreasing is False:
            return False
    return isNonDecresing or isNonIncreasing
         
