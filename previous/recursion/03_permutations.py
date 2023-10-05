# Permutation

"""
Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.

Sample Input
array = [1, 2, 3]


Sample Output

[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]


"""

def getPermutationsHelper(array, permutations=[], currentPermutation=[]):
     # 3 * 2 * 1 = 6
    if len(array) == 0 and len(currentPermutation) > 0:
        permutations.append(currentPermutation)
        return
    for i in range(len(array)):
        newArray = array[:i] + array[i+1:]
        newPermutation = currentPermutation + [array[i]]
        getPermutationsHelper(newArray, permutations, newPermutation)
    return permutations

def getPermutations(array):
    permutations = []
    currentPermutation = []
    return getPermutationsHelper(array, permutations, currentPermutation)


if __name__ == "__main__":
    array = [1, 2, 3]
    permutations__ = getPermutations(array)
    print(permutations__)

    # array = [1, 2, 3, 4]
    # permutations = getPermutations(array)
    # print(permutations)

    # array = [1, 2, 3, 4, 5]
    # permutations = getPermutations(array)
    # print(permutations)