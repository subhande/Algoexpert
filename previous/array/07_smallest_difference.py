# Smallest difference
"""
Write a function that takes in two non-empty arrays of integers, finds the pair
of numbers (one from each array) whose absolute difference is closest to zero,
and returns an array containing these two numbers, with the number from the
first array in the first position.
Note that the absolute difference of two integers is the distance between them
on the real number line. For example, the absolute difference of -5 and 5 is 10,
and the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest
difference.


Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
Sample Output
[28, 26]
"""






# Time: O(n^2) | Space: O(1)
def smallestDifference(arrayOne, arrayTwo):
    smallest = float('inf')
    result = []
    for idx1, item1 in enumerate(arrayOne):
        for idx2, item2 in enumerate(arrayTwo):
            sum = item1-item2 if item1 > item2 else item2-item1
            if sum < smallest:
                smallest = sum
                result = [item1, item2]
    return result

# Time: O(nlogn) | Space: O(1)
def smallestDifference(arrayOne, arrayTwo):
    smallest = float('inf')
    result = []
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    while i < len(arrayOne) and j < len(arrayTwo):
        item1 = arrayOne[i]
        item2 = arrayTwo[j]
        sum = item1-item2 if item1 > item2 else item2-item1
        if sum < smallest:
            smallest = sum
            result = [item1, item2]
        if item1 > item2:
            j += 1
        else:
            i += 1
    return result


if __name__ == "__main__":
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    assert smallestDifference(arrayOne, arrayTwo) == [28, 26]