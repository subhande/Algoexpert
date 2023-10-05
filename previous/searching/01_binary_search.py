# Binary Search
"""
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

Sample Input
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

Sample Output
3



"""

# Iteration Solution
# Time: O(log(n)) | Space: O(1)
def binarySearch(array, target):
    left = 0
    right = len(array)-1
    mid = (left + right) // 2

    while left <= right:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
            mid = (left + right) // 2
        else:
            left = mid + 1
            mid = (left + right) // 2
    return -1

# Recursive Solution
# Time: o(log(n)) | Space: O(log(n))
def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearchHelper(array, target, left, mid-1)
    else:
        return binarySearchHelper(array, target, mid+1, right)

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)