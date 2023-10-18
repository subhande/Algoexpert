# Find Three Largest Numbers
"""
Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].


Sample Input
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output
[18, 141, 541]


"""

# Brute Force Solution
# Time: O(n) | Space: O(1)
def findThreeLargestNumbers(array):
    max_value = max(array)
    max_index = array.index(max_value)
    array.pop(max_index)
    second_max_value = max(array)
    second_max_index = array.index(second_max_value)
    array.pop(second_max_index)
    third_max_value = max(array)
    return [third_max_value, second_max_value, max_value]   


# Optimal Solution
# Time: O(n) | Space: O(1)

def updateLargest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shiftAndUpdate(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shiftAndUpdate(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shiftAndUpdate(three_largest, num, 0)


def shiftAndUpdate(array, num, index):
    for i in range(index+1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i+1]
            
# Time: O(n) | Space: O(1)
def findThreeLargestNumbers(array):
    three_largest = [None, None, None]
    for num in array:
        updateLargest(three_largest, num)
    return three_largest