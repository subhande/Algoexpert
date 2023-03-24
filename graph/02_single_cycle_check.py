# Single Cycle Check

"""
You're given an array of integers where each integer represents a jump of its value in the array. For instance, the integer 2 represents a jump of two indices forward in the array; the integer -3 represents a jump of three indices backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0.


Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back on the starting index.


Sample Input
array = [2, 3, 1, -4, -4, 2]

Sample Output
true

"""
# Brute Force Solution
# Time: O(n) | Space: O(n)
def hasSingleCycle(array):
    visited = [0] * len(array)
    idx = 0
    for _ in range(len(array)):
        if visited[idx] == 1:
            return False
        visited[idx] = 1
        idx = (idx + array[idx]) % len(array)
    if idx != 0:
        return False
    return True



# Optimized Solution
def getNextIdx(idx, array):
    jump = array[idx]
    nextIdx = (idx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


# Time: O(n) | Space: O(1)
def hasSingleCycle(array):
    numElementsVisited = 0
    idx = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and idx == 0:
            return False
        numElementsVisited += 1
        idx = getNextIdx(idx, array)
    return idx == 0
