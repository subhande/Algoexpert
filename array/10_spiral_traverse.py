# Spiral Traverse
"""
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional 
array of all the array's elements in spiral order. Spiral order starts at the top left corner of the two-dimensional 
array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.
Sample Input
array = [
    [1,   2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
]
Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

# Time: O(n^2) | Space: O(1)
def spiralTraverse(array):
    r = 0
    c = 0
    r_max = len(array)
    c_max = len(array[0]) 
    visited = []

    if r_max == 1:
        return array[0]
    if c_max == 1:
        return [array[i][0] for i in range(r_max)]

    while r < r_max or c < c_max:
        # Moving left
        print("Left")
        print(r, r_max, c, c_max, list(range(c, c_max)), visited)
        if r >= r_max or c >= c_max:
            break
        for i in range(c, c_max):
            visited.append(array[r][i])
        r += 1
        print("Down")
        print(r, r_max, c, c_max, list(range(r, r_max)), visited)
        # Moving downward
        if r >= r_max or c >= c_max:
            break
        for i in range(r, r_max):
            visited.append(array[i][c_max - 1])
        c_max -= 1
        print("right")
        print(r, r_max, c, c_max, list(range(c_max - 1, c - 1, -1)), visited)
        # Moving right
        if r >= r_max or c >= c_max:
            break
        for i in range(c_max - 1, c - 1, -1):
            visited.append(array[r_max - 1][i])
        r_max -= 1
        print("Up")
        print(r, r_max, c, c_max, list(range(r_max - 1, r - 1, -1)), visited)
        # Moving Up
        if r >= r_max or c >= c_max:
            break
        for i in range(r_max - 1, r - 1, -1):
            visited.append(array[i][c])
        c += 1
    return visited


if __name__ == "__main__":
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    expected = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
    ]
    assert spiralTraverse(array) == expected, f"Expected {expected}, but got {spiralTraverse(array)}"

    array = [
        [1, 2, 3, 4], 
        [10, 11, 12, 5], 
        [9, 8, 7, 6]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    assert spiralTraverse(array) == expected, f"Expected {expected}, but got {spiralTraverse(array)}"
