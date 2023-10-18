# BST Traversal

"""
Write three functions that take in a Binary Search Tree (BST) and an empty array, traverse the BST, add its nodes' values to the input array, and return that array. The three functions should traverse the BST using the in-order, pre-order, and post-order tree-traversal techniques, respectively.

If you're unfamiliar with tree-traversal techniques, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

Sample Input
tree =             10
                 /    \
                5      15
               / \    /  \
              2   5  13  22
             /        \
            1          14

"""

# Time: O(n)  | Space: O(n)
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

# Time: O(n)  | Space: O(n)
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
        
    return array

# Time: O(n)  | Space: O(n)
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
