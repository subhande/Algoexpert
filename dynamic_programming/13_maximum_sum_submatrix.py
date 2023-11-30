# Maximum Sum Submatrix

"""

You're given a two-dimensional array (a matrix) of potentially unequal height and width that's filled with integers.

You're also given a positive integer size. Write a function that returns the maximum sum that can be generated from a submatrix with dimensions size * size.

For example, consider the following matrix:

[
    [2, 4],
    [5, 6],
    [-3, 2],
]

If size = 2, then the 2x2 submatrices to consider are:

    [[2, 4],
    [5, 6]]
    --------
    [[5, 6],
    [-3, 2]]

The sums of the elements in the first submatrix is 17, and the sum of the elements in the second submatrix is 10. In this example, your function should return 17.

Note: size will always be at least 1, and the dimensions of the input matrix will always be at least size * size.


Sample Input
matrix = [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2],
]
size = 2

Sample Output
18
// [ 
//   [., ., ., .],
//   [., 3, 7, .],
//   [., 8, 0, .],
//   [., ., ., .],
// ]



"""


# Solution 1: Brute Force
# Time: O(whs^2) | Space: O(1) where s is size of submatrix


def matrix_sum(matrix, i, j, size):
    subMatrixSum = 0
    for r in range(i, i + size):
        for c in range(j, j + size):
            subMatrixSum += matrix[r][c]
    return subMatrixSum


def maximumSumSubmatrix(matrix, size):
    n = len(matrix)
    m = len(matrix[0])

    maxSumOfSubMatrix = float("-inf")

    if n == 1 and m == 1 and size == 1:
        return matrix[0][0]

    for i in range(0, n - size + 1):
        for j in range(0, m - size + 1):
            print([i, j, i + size - 1, j + size - 1, n - 1, m - 1])
            sumOfSubMatrix = matrix_sum(matrix, i, j, size)
            if sumOfSubMatrix > maxSumOfSubMatrix:
                maxSumOfSubMatrix = sumOfSubMatrix

    return maxSumOfSubMatrix


# Solution 2: Algoexpert
# Time: O(wh) | Space: O(wh)

def createSumMatric(matrix):
    sums = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    sums[0][0] = matrix[0][0]

    # Fill the first row
    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]

    # Fill the first col
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]

    # Fill the rest of the matrix
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]
    return sums


def maximumSumSubmatrix(matrix, size):
    sums = createSumMatric(matrix)
    maxSumOfSubMatrix = float("-inf")

    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]

            touchesTopBorder = row - size < 0
            if not touchesTopBorder:
                total -= sums[row - size][col]

            touchesLeftBorder = col - size < 0
            if not touchesLeftBorder:
                total -= sums[row][col - size]

            touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder

            if not touchesTopOrLeftBorder:
                total += sums[row - size][col - size]

            maxSumOfSubMatrix = max(maxSumOfSubMatrix, total)

    return maxSumOfSubMatrix


if __name__ == "__main__":
    matrix = [[3, -4, 6, -5, 1], [1, -2, 8, -4, -2], [3, -8, 9, 3, 1], [-7, 3, 4, 2, 7], [-3, 7, -5, 7, -6]]
    size = 3
    maxSumOfSubMatrix = maximumSumSubmatrix(matrix, size)
    print(f"maxSumOfSubMatrix: ", maxSumOfSubMatrix)
