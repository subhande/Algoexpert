# Array of products
"""
Write a function that takes in a non-empty array of integers and returns an array of the same length, where 
each element in the output array is equal to the product of every other number in the input array.
In other words, the value at output[i] is equal to the product of every number in the input array other 
than input[i].
Note that you're expected to solve this problem without using division.
Sample Input
array = [5, 1, 4, 2]
Sample Output
[8, 40, 10, 20] # 8 is equal to 1 x 4 x 2, 40 is equal to 5 x 4 x 2, 10 is equal to 5 x 1 x 2, 20 is equal to 5 x 1 x 4


"""

# Time: 0(n) | Space: O(1)
def arrayOfProducts(array):
    products = []
    for i in range(len(array)):
        currentProduct = 1
        for j in range(len(array)):
            if i != j:
                currentProduct = currentProduct * array[j]
        products.append(currentProduct)
    return products

# Time: 0(n) | Space: O(1)
def arrayOfProducts(array):
    leftProduct = [1 for _ in range(len(array))]
    rightProduct = [1 for _ in range(len(array))]
    products = [1 for _ in range(len(array))]
    leftRunningProduct = 1
    for i in range(len(array)):
        leftProduct[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProduct[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
       products[i] = leftProduct[i] * rightProduct[i]
    return products


# Time: 0(n) | Space: O(1)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]
    return products


if __name__ == "__main__":
    array = [5, 1, 4, 2]
    print(arrayOfProducts(array))