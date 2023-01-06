# First Duplicate Value
"""
Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should return -1.

Note that you're allowed to mutate the input array.

Sample Input
array = [2, 1, 5, 2, 3, 3, 4]

Sample Output
2 // 2 is the first integer that appears more than once.

"""
# Time: O(n) | Space: O(n)
def firstDuplicateValue(array):
    frequency = {}
    for i in array:
        if frequency.get(i):
            return i
        else:
            frequency[i] = 1
    return -1

##  Below solution only works when following criteria met
# 1. Given an array of integers between 1 and n, inclusive, where n is the length of the array
# 2. Note that you're allowed to mutate the input array.

# Time: O(n) | Space: O(1)
def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue-1] < 0:
            return absValue
        array[absValue-1] *= -1
    return -1